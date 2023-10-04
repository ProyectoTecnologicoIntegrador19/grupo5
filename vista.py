import controlador

while True:
        menu = input("""\nIngrese número: 1) Tendencias   2) Tendencias Developer   3) Perfil   9) Salir \n     """)
        if menu == "1":#TENDENCIAS-----------------------------------------------------------------------------------------------------
            menuTendencias = input("""\nTendencias:  1) Mensual   2) Semanal   3) Diaria \n     """)
            if menuTendencias == "1": controlador.listarTendenciasMensuales ()#llama al archivo controlador y el metodo que que se necesita mostrar
            if menuTendencias == "2": controlador.listarTendenciasSemanales ()
            if menuTendencias == "3": controlador.listarTendenciasDiarias ()
        elif menu == "2":#TENDENCIAS DEVELOPER-------------------------------------------------------------------------------------------
            menuTendDeveloper = input("""\nTendencias Developer:  1) Mensual   2) Semanal   3) Diaria \n     """)
            if menuTendDeveloper == "1": controlador.listarTendDeveloperMensuales ()
            if menuTendDeveloper == "2": controlador.listarTendDeveloperSemanales ()
            if menuTendDeveloper == "3": controlador.listarTendDeveloperDiarias ()
        elif menu == "3":#PERFIL-----------------------------------------------------------------------------------------------------
            controlador.listarInformacionPerfil ()    
        
        elif menu == "9":#SALIR    
            print("\n OFF."); exit()
        else: print("\nOpcion no valida")
        
        