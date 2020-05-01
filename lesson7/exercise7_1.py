'''Понимаю, что ОЧЕНЬ грамоздкий код получился - очень непросто мне сразу всё сообразить'''
class Matrix:
    #matrix_count = 0
    def __init__(self, var_list):
        #self.out = var_list
        self.param_1 = var_list[0]
        self.param_1_1 = int(self.param_1[0])
        self.param_1_2 = int(self.param_1[1])
        self.param_1_3 = int(self.param_1[2])

        self.param_2 = var_list[1]
        self.param_2_1 = int(self.param_2[0])
        self.param_2_2 = int(self.param_2[1])
        self.param_2_3 = int(self.param_2[2])

        self.param_3 = var_list[2]
        self.param_3_1 = int(self.param_3[0])
        self.param_3_2 = int(self.param_3[1])
        self.param_3_3 = int(self.param_3[2])

        #Matrix.matrix_count +=1

    def __str__(self):

        return print('\n',str(self.param_1_1),' ', str(self.param_1_2),' ',str(self.param_1_3),'\n',
                     str(self.param_2_1),' ', str(self.param_2_2),' ',str(self.param_2_3),'\n',
                     str(self.param_3_1),' ', str(self.param_3_2),' ',str(self.param_3_3),'\n')

    def __add__(self, other):
        self.param_t_1_1 = self.param_1_1 + other.param_1_1
        self.param_t_1_2 = self.param_1_2 + other.param_1_2
        self.param_t_1_3 = self.param_1_3 + other.param_1_3
        #self.param_t_1 = [self.param_t_1_1, self.param_t_1_2, self.param_t_1_3]

        self.param_t_2_1 = self.param_2_1 + other.param_2_1
        self.param_t_2_2 = self.param_2_2 + other.param_2_2
        self.param_t_2_3 = self.param_2_3 + other.param_2_3
        #self.param_t_2 = [self.param_t_2_1, self.param_t_2_2, self.param_t_2_3]

        self.param_t_3_1 = self.param_3_1 + other.param_3_1
        self.param_t_3_2 = self.param_3_2 + other.param_3_2
        self.param_t_3_3 = self.param_3_3 + other.param_3_3
        #self.param_t_3 = [self.param_t_3_1, self.param_t_3_2, self.param_t_3_3]

        #var_list_total = [self.param_t_1, self.param_t_2, self.param_t_3]
        #var_c =Matrix(var_list_total)
        return print('\n',str(self.param_t_1_1),' ', str(self.param_t_1_2),' ',str(self.param_t_1_3),'\n',
                     str(self.param_t_2_1),' ', str(self.param_t_2_2),' ',str(self.param_t_2_3),'\n',
                     str(self.param_t_3_1),' ', str(self.param_t_3_2),' ',str(self.param_t_3_3),'\n')
                      #self.param_1_1 + other.param_1_1,
                      #self.param_1_2 + other.param_1_2,
                      #self.param_1_3 + other.param_1_3,
                      #self.param_2_1 + other.param_2_1,
                      #self.param_2_2 + other.param_2_2,
                      #self.param_2_3 + other.param_2_3,
                      #self.param_3_1 + other.param_3_1,
                      #self.param_3_2 + other.param_3_2,
                      #self.param_3_3 + other.param_3_3
                      #)


var_list_a_1 = [1, 2, 3]
var_list_a_2 = [4, 5, 6]
var_list_a_3 = [7, 8, 9]
var_list_a = [var_list_a_1, var_list_a_2, var_list_a_3]

var_list_b_1 = [10, 10, 10]
var_list_b_2 = [10, 10, 10]
var_list_b_3 = [10, 10, 10]
var_list_b = [var_list_b_1, var_list_b_2, var_list_b_3]

var_a = Matrix(var_list_a)
var_b = Matrix(var_list_b)
#print(var_a.out)
#print(var_b.out)
var_a.__str__()
var_b.__str__()
var_a + var_b

