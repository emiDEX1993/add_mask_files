"""Add_mask script by Emilio Sarabia Valverde
--------------------------------------------
may 30th, 2024 --version v01"""



import nuke



#def function for item command
def add_mask():

    n = nuke.selectedNode()
#setting of variables to know which input number corresponds to the mask. Default value set to 1
    mask_input_number = 1
    node_inputs = {"Merge2":2,
                    "ChannelMerge":2,
                    "Copy":2,
                    }
    node_class = n.Class()

    if node_class in node_inputs:
        mask_input_number = node_inputs[node_class]
    
#if mask input is already in use, notifies the user
    if n.input(mask_input_number):
        nuke.message("the mask is already connected")
        return

#ask the user whath kind of mask need
    user_choice = nuke.choice("type of mask","choose your mask",["Roto","Paint"])

#changes which nodes it connects to the mask depending on the user's choice
    if user_choice == 0 and n.input(mask_input_number) == None:
        roto = nuke.nodes.Roto()
        dot = nuke.nodes.Dot()
        blur = nuke.nodes.Blur()

        roto.setXYpos(n.xpos()+120,n.ypos()-100)
        dot.setYpos(int(n.ypos()
                            +n.screenHeight()/2
                            -dot.screenHeight()/2
                             ) )
        dot.setXpos(int(n.xpos()+120
                            +n.screenWidth()/2
                            -dot.screenWidth()/2
                            ) )

        blur.setInput(0,roto)
        dot.setInput(0,blur)
        n.setInput(mask_input_number,dot)
    
        
    if user_choice ==1 and n.input(mask_input_number) ==None:
        paint = nuke.nodes.RotoPaint()
        dot = nuke.nodes.Dot()
        paint.setXYpos(n.xpos()+120,n.ypos()-100)
        dot.setYpos(int(paint.ypos()+100
                            +paint.screenHeight()/2
                            -dot.screenHeight()/2
                            ) )
        dot.setXpos(int(n.xpos()+120
                            +n.screenWidth()/2
                            -dot.screenWidth()/2
                            ) )

        dot.setInput(0,paint)
        n.setInput(mask_input_number,dot)
  
 
#set the item command
nuke.menu("Nuke").addCommand("Edit/Add mask",add_mask,shortcut = "Ctrl+m",shortcutContext = 2)