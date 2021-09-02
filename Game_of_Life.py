from prettytable import PrettyTable as PT 
from time import sleep

class Game_of_Life:
    board_layout = [
        ["-","*","-","-","-","-","*","*"],
        ["-","*","*","-","*","-","-","*"],
        ["-","-","-","*","*","*","-","-"],
        ["-","-","-","-","-","-","-","-"],
        ["-","*","-","-","-","-","*","*"],
        ["-","*","*","-","*","-","-","*"],
        ["-","-","-","*","*","*","-","-"],
        ["-","-","-","-","-","-","-","-"]]
    alive_pos_list = []
    neighbor_dic = {}
    possible_new_life_list = []
    gen_count = 1
    size_x = len(board_layout)
    size_y = len(board_layout[0])
    
    def Check_Pos(self):
        i = 0
        self.alive_pos_list = []
        while i < self.size_x:
            ii = 0
            while ii < self.size_y:
                if self.board_layout[i][ii] == "*":
                    pos_true = [i,ii]
                    self.alive_pos_list.append(pos_true)
                ii += 1
            i += 1

    def Check_Neighbors(self):
        self.neighbor_dic = {}
        for i in self.alive_pos_list:
            num_neighbors = 0
            temp_neighbors = []
            for temp_pos in self.alive_pos_list:
                if i[0] == temp_pos[0] and (i[1]+1 == temp_pos[1] or i[1]-1 == temp_pos[1]):
                    temp_neighbors.append(temp_pos)
                    num_neighbors += 1
                elif i[1] == temp_pos[1] and (i[0]+1 == temp_pos[0] or i[0]-1 == temp_pos[0]):
                    temp_neighbors.append(temp_pos)
                    num_neighbors += 1 
                elif (i[0]+1 == temp_pos[0] and i[1]+1 == temp_pos[1]) or (i[0]-1 == temp_pos[0] and i[1]+1 == temp_pos[1]):
                    temp_neighbors.append(temp_pos)
                    num_neighbors += 1
                elif (i[0]+1 == temp_pos[0] and i[1]-1 == temp_pos[1]) or (i[0]-1 == temp_pos[0] and i[1]-1 == temp_pos[1]):
                    temp_neighbors.append(temp_pos)
                    num_neighbors += 1

            self.neighbor_dic[tuple(i)] = tuple(temp_neighbors)
    
    def Check_Possible_New_life_Locations(self):
        self.possible_new_life_list = []
        for i in self.alive_pos_list:
            temp_new_pos = [i[0]-1,i[1]-1]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)            
            temp_new_pos = [i[0],i[1]-1]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)
            temp_new_pos = [i[0]-1,i[1]]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)
            temp_new_pos = [i[0]-1,i[1]+1]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)
            temp_new_pos = [i[0]+1,i[1]+1]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)
            temp_new_pos = [i[0],i[1]+1]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)
            temp_new_pos = [i[0]+1,i[1]]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)
            temp_new_pos = [i[0]+1,i[1]-1]
            if temp_new_pos not in self.alive_pos_list:
                self.possible_new_life_list.append(temp_new_pos)

        for i in self.possible_new_life_list:
            temp_list = self.possible_new_life_list
            x, y = i
            if (x > self.size_x - 1 or y > self.size_y - 1) or (x < 0 or y < 0):
                temp_list.remove(i)

        self.possible_new_life_list = temp_list
    
    def Check_Still_Alive(self):
        temp_del_list = []
        for life in self.neighbor_dic.keys():
            value = self.neighbor_dic[life]
            if len(value) < 2 or len(value) > 3:
                temp_del_list.append(list(life))

        for life in temp_del_list:
            life_list = list(life)
            self.alive_pos_list.remove(life_list)
            del self.neighbor_dic[tuple(life)]
            x = life_list[0]
            y = life_list[1]

            self.board_layout[x][y] = '-'

    def Create_New_Life(self):
        for i in self.possible_new_life_list:
            alive_neigbor_count = self.possible_new_life_list.count(i)

            if alive_neigbor_count == 3 and i not in self.alive_pos_list:
                self.alive_pos_list.append(i)

    def Update_View(self):
        for i in self.alive_pos_list:
            x = i[0]
            y = i[1]

            self.board_layout[x][y] = '*'

if __name__ == '__main__':
    Gf = Game_of_Life()
    while True:
        Gf.Check_Pos()
        Gf.Check_Neighbors()
        Gf.Check_Possible_New_life_Locations()
        Gf.Check_Still_Alive()
        Gf.Create_New_Life()
        Gf.Update_View()
        
        draw = PT()
        draw.add_rows(Gf.board_layout)
        print("Generation: " + str(Gf.gen_count))
        print(draw)

        Gf.gen_count += 1
        sleep(2)