from Graphic.pieces import *

class Board(object):
    board = []    
    def __init__(self , team): 
        self.reset_board(team)
        self.templates = {'wood' : 0 , 'normal' : 1}
        self.selected_tempelate = 0
        self.template_path = [['1' , '2'],['3' , '4']]
        

    def set_template(self , selecte):
        self.selected_tempelate = self.templates[selecte]
        
    def reset_board(self , team):
        if team == 'black':
            Board.board = [['w_rook','w_knight','w_bishop','w_king','w_queen','w_bishop','w_knight','w_rook'],
                    ['w_pawn','w_pawn','w_pawn','w_pawn','w_pawn','w_pawn','w_pawn','w_pawn'],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    ['b_pawn','b_pawn','b_pawn','b_pawn','b_pawn','b_pawn','b_pawn','b_pawn'],
                    ['b_rook','b_knight','b_bishop','b_queen','b_king','b_bishop','b_knight','b_rook']
                ]
        else :
            Board.board = [['b_rook','b_knight','b_bishop','b_queen','b_king','b_bishop','b_knight','b_rook'],
                    ['b_pawn','b_pawn','b_pawn','b_pawn','b_pawn','b_pawn','b_pawn','b_pawn'],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    ['w_pawn','w_pawn','w_pawn','w_pawn','w_pawn','w_pawn','w_pawn','w_pawn'],
                    ['w_rook','w_knight','w_bishop','w_king','w_queen','w_bishop','w_knight','w_rook']
                ]    
 
    def draw_board(self): 
        BRIGHT = Pieces()
        BRIGHT.set_background(self.template_path[self.selected_tempelate][0])
        DARK = Pieces()
        DARK.set_background(self.template_path[self.selected_tempelate][1]) 
        i = 0
        for y in range(0, height, int(height / 8)):
            i+=1
            for x in range(0, width, int(width / 8)):
                i+=1
                if(i%2 == 0):
                    BRIGHT.draw_model([x , y])
                else:
                    DARK.draw_model([x , y])              
                
    def draw_piece(self):
        p = Pieces()
        for x in range(0 , 8):
            for y in range(0 , 8):
                if not Board.board[x][y] == 0:
                    name = str(Board.board[x][y])
                    p.set_model(name)
                    p.draw_model([ y *100 , x * 100])
