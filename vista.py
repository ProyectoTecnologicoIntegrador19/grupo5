import controlador 

while True:
        menu = input("""\nIngrese número: 1) Tendencias      8) Perfil   9) Salir \n     """)
        if menu == "1":#TENDENCIAS-----------------------------------------------------------------------------------------------------
            menuTendencias = input("""\nTendencias:  1) Mensual   2) Semanal   3) Diaria \n             """)
            if menuTendencias == "1": controlador.listarTendenciasMensuales ()#llama al archivo controlador y el metodo que que se necesita mostrar
            if menuTendencias == "2": controlador.listarTendenciasSemanales ()
            if menuTendencias == "3": controlador.listarTendenciasDiarias ()
        if menu == "8":#PERFIL-----------------------------------------------------------------------------------------------------
            controlador.listarInformacionPerfil ()
        
        elif menu == "9":#SALIR    
            print("\n OFF."); exit()
        else: 
            print("\nOpcion no valida")
        
        
           
        