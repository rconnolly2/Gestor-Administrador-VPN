import pygame

class gestor:
    def __init__(self, tamaño_pantalla, color_fondo):
        self.tamaño_pantalla = tamaño_pantalla
        self.color_fondo = color_fondo
        self.color_barra_menu = (29, 79, 113)
        self.running = True


        #Seccion pygame
        try:
            self.pantalla = pygame.display.set_mode((self.tamaño_pantalla))
        except:
            print("Error: Datos de tamaño_pantalla no valido comprueba que el formato este bien ej: (500, 500)")

        #Logo nord
        try:
            self.logo_nord = pygame.image.load("nordvpn.png")
            self.logo_nord = pygame.transform.scale(self.logo_nord, (self.tamaño_pantalla[1]/9, self.tamaño_pantalla[1]/9))
        except:
            print("Error: Fallo al caragar imagen esta en la misma carpeta ?")

        pygame.display.set_caption("Gestor de Administrador NordRobertVPN")

    def CTodasPaginas(self):
        # Esta funcion carga graficamente lo que hay en todas las pagina por ejemplo la barra del menu
        # Cargamos fondo del color seleccionado:
        self.pantalla.fill(self.color_fondo)
        # Ahorra fondo barra menu
        pygame.draw.rect(self.pantalla, self.color_barra_menu, (0, 0, self.tamaño_pantalla[0], self.tamaño_pantalla[1]/9))
        #Imprimimos el logo de nord
        self.pantalla.blit(self.logo_nord, (0, 0))

    def BuclePrograma(self):
        while self.running == True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False
                    # Si le damos al boton de cerrar ventana, cerramos programa

            # Si no actulizamos pantalla
            pygame.display.flip()

    






Objeto1 = gestor((700, 500), (232, 232, 232))
Objeto1.CTodasPaginas()
Objeto1.BuclePrograma()
