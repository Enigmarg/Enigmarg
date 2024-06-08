import pygame

class Level:
    def __init__(self, screen, transition_call):
        """
        Inicializa um objeto Level.

        Args:
            screen (pygame.Surface): A superfície para renderizar o nível.

        Attributes:
            screen (pygame.Surface): A superfície para renderizar o nível.
            is_active (bool): Indica se o nível está ativo no momento.
            is_loaded (bool): Indica se o nível foi carregado.
        """
        self.is_active: bool = False
        self.is_loaded: bool = False
        self.screen: pygame.Surface = screen
        self.transition_call = transition_call

    def load(self):
        """
        Carrega os dados do nível
        """

    def run(self):
        """
        Este método é responsável por executar a lógica do nível.
        """

    def get_status(self) -> bool:
        """
        Retorna o status do objeto.

        Returns:
            bool: O status do objeto.
        """
        return self.is_active
