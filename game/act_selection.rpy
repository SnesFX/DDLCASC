label act_selection:
    scene black
    "Here's some silly selection code for you to choose one of the Acts."
    "Made by: SnesFX"
    
    menu:
        "Choose your favorite Doki."
        
        "Act 1":
            call ch0_main from _call_ch0_main
        "Act 2":
            call ch20_main from _call_ch20_main
        #"Act 3":
        #    call ch30_main from _call_ch30_main
    return