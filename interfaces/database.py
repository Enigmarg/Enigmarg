from dotenv import load_dotenv
import os
import json
import mysql.connector

load_dotenv()

class Database():
    def __init__(self):
        self.host = os.getenv("HOST")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.database = os.getenv("DATABASE")
        self.port = os.getenv("PORT")

    # Tenta fazer a conexão com o banco de dados.
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                database = self.database,
                port = self.port,
            )
            print("Conexão bem sucedida!")
            self.cursor = self.cnx.cursor(buffered=True)
            return self.cnx
        except mysql.connector.Error as err:
            print(f"Falha na conexão! {err}")
            return None
        
    # Pega e retorna o usuário do banco de dados.
    def get_user(self, email:str, password:str):
        try:
            sql = ("SELECT user_id, user_email, user_password FROM tb_user WHERE user_email='%s' AND user_password='%s'" % (email, password))
            self.cursor.execute(sql)
            self.cnx.commit()
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            print(e)
            return None
            
    # Pega e retorna o email do usuário do banco de dados.
    def get_user_email(self, email:str):
        try:
            sql = ("SELECT tb_user.user_email FROM tb_user WHERE tb_user.user_email='%s'" % email)
            self.cursor.execute(sql)
            self.cnx.commit()
            email = self.cursor.fetchone()[0]
            return email
        except Exception as e:
            print(e)

    # Pega e retorna o cargo do usuário do banco de dados.
    def get_user_role(self, email:str):
        try:
            sql = ("SELECT tb_role.role_name FROM tb_role JOIN tb_user ON tb_role.role_id = tb_user.role_id WHERE tb_user.user_email='%s'" % email)
            self.cursor.execute(sql)
            self.cnx.commit()
            role = self.cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        
    # Pega e retorna todos os usuários do banco de dados.
    def get_all_users(self):
        try:
            sql = ("SELECT tb_user.user_email, role_name FROM tb_role INNER JOIN tb_user ON tb_user.role_id = tb_role.role_id WHERE role_name != 'Admin'")
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            self.cnx.commit()
            return users
        except Exception as e:
            print(e)
        
    # Adiciona um usuário ao banco de dados.
    def add_user(self, email:str, password:str, role:str):
        try:
            sql = ("INSERT INTO tb_user (user_email, user_password, role_id) SELECT '%s', '%s', role_id FROM tb_role WHERE tb_role.role_name = '%s'" % (email, password, role))
            self.cursor.execute(sql)
            self.cnx.commit()
        except Exception as e:
            print(e)

    # Atualiza um usuário no banco de dados.
    def update_user(self, email:str, password:str, role:str):
        try:
            if (email and password and role):
                sql = ("UPDATE tb_user JOIN tb_role ON tb_role.role_name = '%s' SET tb_user.user_email = '%s', tb_user.user_password = '%s', tb_user.role_id = tb_role.role_id WHERE tb_user.user_email = '%s'" % (role, email, password, email))
                self.cursor.execute(sql)
                self.cnx.commit()
            elif (email and role):
                sql = ("UPDATE tb_user JOIN tb_role ON tb_role.role_name = '%s' SET tb_user.user_email = '%s', tb_user.role_id = tb_role.role_id WHERE tb_user.user_email = '%s'" % (role, email, email))
                self.cursor.execute(sql)
                self.cnx.commit()
        except Exception as e:
            print(e)

    # Deleta um usuário do banco de dados.
    def delete_user(self, email:str):
        try:
            sql = ("DELETE FROM tb_user WHERE user_email = '%s'" % email)
            self.cursor.execute(sql)
            self.cnx.commit()
        except Exception as e:
            print(e)

        # tb_question.question_text, tb_answer.answer_text, tb_answer.is_true
        # Pega e retorna todas as questões do banco de dados no formato JSON.
    def get_all_questions_json(self) -> str:
        try:
            """
                Create an sql query that returns all questions and their answers like this:
                {
                    "id": 0,
                    "question": "Qual dessas opções é um tópico que deve ser abordado no parágrafo introdutório de redação modelo ENEM?",
                    "answers": [
                    {
                        "id": 0,
                        "text": "Repertório de abertura",
                        "correct": true
                    },
                    {
                        "id": 1,
                        "text": "Tese",
                        "correct": false
                    },
                    {
                        "id": 2,
                        "text": "Conclusão do texto",
                        "correct": false
                    },
                    {
                        "id": 3,
                        "text": "Argumentação detalhada",
                        "correct": false
                    }
                    ]
                },
            """
            sql = ("""
                SELECT tb_question.question_id, tb_question.question_text,
                    JSON_ARRAYAGG(JSON_OBJECT('answer_id', tb_answer.answer_id, 'answer_text', tb_answer.answer_text, 'is_true', tb_answer.is_true)) AS answers
                FROM tb_question
                JOIN tb_answer ON tb_question.question_id = tb_answer.question_id
                GROUP BY tb_question.question_id
            """)

            self.cursor.execute(sql)
            questions = self.cursor.fetchall()
            self.cnx.commit()
            questions_json = []
            for question in questions:
                question_dict = {
                    "id": question[0],
                    "question": question[1],
                    "answers": []
                }
                answers = json.loads(question[2])
                for answer in answers:
                    answer_dict = {
                        "id": answer["answer_id"],
                        "text": answer["answer_text"],
                        "correct": answer["is_true"]
                    }
                    question_dict["answers"].append(answer_dict)
                questions_json.append(question_dict)

            return json.dumps(questions_json)
        except Exception as e:
            print(e)
            return "Error getting questions!"
    
    # Adiciona uma questão ao banco de dados.
    def add_question(self, question:str, alter1:str, alter2:str, alter3:str, answer:str):
        try:
            self.cursor.execute("INSERT INTO tb_question (question_text) SELECT '%s'" % (question))
            question_id = self.cursor.lastrowid
            self.cursor.executemany("INSERT INTO tb_answer (answer_text, is_true, question_id) VALUES (%s, %s, %s)", [(alter1, 0, question_id), (alter2, 0, question_id), (alter3, 0, question_id), (answer, 1, question_id)])
            self.cnx.commit()
            print("Questão adicionada!")
        except Exception as e:
            print(e)

    # Atualiza uma questão do banco de dados.
    def update_question(self, question_id:str, question:str, alter1:str, alter2:str, alter3:str, answer):
        try:
            self.cursor.execute("START TRANSACTION")

            # Atualiza a pergunta da questão.
            sql1 = ("UPDATE tb_question SET question_text = '%s' WHERE question_id = %s" % (question, question_id))
            self.cursor.execute(sql1)

            # Atualiza cada alternativa individualmente.
            sql2 = ("""
                UPDATE tb_answer
                JOIN (
                    SELECT 
                        question_id, answer_id, answer_text,
                        ROW_NUMBER() OVER (PARTITION BY question_id ORDER BY is_true ASC) AS rn
                    FROM tb_answer
                    WHERE question_id = %s
                ) AS subquery
                ON tb_answer.answer_id = subquery.answer_id
                SET tb_answer.answer_text = 
                    CASE 
                        WHEN subquery.rn = 1 THEN '%s'
                        WHEN subquery.rn = 2 THEN '%s'
                        WHEN subquery.rn = 3 THEN '%s'
                        WHEN subquery.rn = 4 THEN '%s'
                    END
            """ % (question_id, alter1, alter2, alter3, answer))
            self.cursor.execute(sql2)
            self.cnx.commit()
        except Exception as e:
                print(e)

    # Deleta uma questão do banco de dados.
    def delete_question(self, question_id:int):
        try:
            sql = ("DELETE FROM tb_question WHERE question_id = '%s'" % (question_id))
            self.cursor.execute(sql)
            self.cnx.commit()
        except Exception as e:
            print(e)

        # Pega todas as questões do banco de dados.
    def get_all_questions(self):
        try:
            sql = ("""
                SELECT tb_question.question_id, tb_question.question_text AS pergunta,
                    (SELECT answer_text FROM tb_answer WHERE question_id = tb_question.question_id ORDER BY is_true ASC LIMIT 1 OFFSET 0) AS alternativa,
                    (SELECT answer_text FROM tb_answer WHERE question_id = tb_question.question_id ORDER BY is_true ASC LIMIT 1 OFFSET 1) AS alternativa,
                    (SELECT answer_text FROM tb_answer WHERE question_id = tb_question.question_id ORDER BY is_true ASC LIMIT 1 OFFSET 2) AS alternativa,
                (SELECT answer_text FROM tb_answer WHERE question_id = tb_question.question_id ORDER BY is_true ASC LIMIT 1 OFFSET 3) AS resposta
            FROM tb_question
            """)
            self.cursor.execute(sql)
            questions = self.cursor.fetchall()
            self.cnx.commit()
            return questions
        except Exception as e:
            print(e)

    # Adiciona ou atualiza um usuário no ranking.
    def add_score(self, user_id:int, score:int):
        print(user_id, score)
        try:
            sql = ("SELECT * FROM tb_ranking WHERE user_id = %s" % (user_id))
            self.cursor.execute(sql)
            self.cnx.commit()
            user = self.cursor.fetchone()
            print(user)
            if user:
                sql = ("UPDATE tb_ranking SET score = %s WHERE user_id = %s" % (score, user_id))
                self.cursor.execute(sql)
                self.cnx.commit()
            else:
                sql = ("INSERT INTO tb_ranking (user_id, score) VALUES (%s, %s)" % (user_id, score))
                self.cursor.execute(sql)
                self.cnx.commit()
        except Exception as e:
            print(e)
    
    # Pega o email dos 5 primeiros colocados do ranking.
    def get_email_ranking(self):
        try:
            sql = ("SELECT tb_user.user_email FROM tb_user JOIN tb_ranking ON tb_user.user_id = tb_ranking.user_id ORDER BY score DESC LIMIT 5")
            self.cursor.execute(sql)
            emails = self.cursor.fetchall()
            self.cnx.commit()
            return emails
        except Exception as e:
            print(e)
    
    # Pega a pontuação dos 5 primeiros colocados do ranking.
    def get_score_ranking(self):
        try:
            sql = ("SELECT tb_ranking.score FROM tb_ranking JOIN tb_user ON tb_ranking.user_id = tb_user.user_id ORDER BY score DESC LIMIT 5")
            self.cursor.execute(sql)
            emails = self.cursor.fetchall()
            self.cnx.commit()
            return emails
        except Exception as e:
            print(e)