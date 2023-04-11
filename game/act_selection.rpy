label act_selection:
    scene black
    "Here's some silly selection code for you to choose one of the Acts."
    "Also uhh act 3 is hella broken and I'm working on fixing that."
    "Made by: SnesFX"
    
    menu:
        "Choose an Act."
        
        "Act 1":
            call ch0_main from _call_ch0_main
        "Act 2":
            call ch20_main from _call_ch20_main
        #"Act 3":
        #    call ch30_main from _call_ch30_main
    return