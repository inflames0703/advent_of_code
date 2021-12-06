import copy

with open('day_4.txt', 'r') as f:
    numbers = f.readline().split(',')
    bingo_boards_dump = []
    for lines in f:
        for i in range(5):
            bingo_boards_dump.append(f.readline().split())
            
NO_OF_BINGO_BOARDS = int(len(bingo_boards_dump)/5)
bingo_boards_list = []

N = 0
for bingo_board in range(NO_OF_BINGO_BOARDS):
    bingo_boards_list.append(bingo_boards_dump[N:N+5])
    N +=5
    
numbers = [int(i) for i in numbers]
bingo_boards_check_list = copy.deepcopy(bingo_boards_list)
bingo_boards_result_list = [[[0 for i in range(5)] for j in range(2)] for k in range(NO_OF_BINGO_BOARDS)]

for bingo_board in range(NO_OF_BINGO_BOARDS):
    for row in range(5):
        for i in range(5):
            bingo_boards_list[bingo_board][row][i] = int(bingo_boards_list[bingo_board][row][i])
            bingo_boards_check_list[bingo_board][row][i] = 0
            
def find_last_victory_board(numbers, bingo_boards_list):
    boards_bin = []
    for number in numbers:
        for bingo_board in range(NO_OF_BINGO_BOARDS):
            for row in range(5):
                for i in range(5):
                    #print(bingo_boards_list[bingo_board][row][i])
                    if number == bingo_boards_list[bingo_board][row][i]:
                        bingo_boards_check_list[bingo_board][row][i] = 1
                        score = check_bingo_board(bingo_boards_check_list[bingo_board])

                        if score == 1:
                            #print(number, bingo_board)
                            if bingo_board not in boards_bin:
                                boards_bin.append(bingo_board)
                            if len(boards_bin) == NO_OF_BINGO_BOARDS:
                                return (number, bingo_boards_list[bingo_board], bingo_boards_check_list[bingo_board])
                                break
                            
                    
def check_bingo_board(bingo_board):
    for row in bingo_board:

        if sum(row) == 5:
            score = 1
            return score
            break
        
        else:
            score = 0
    for column in range(5): 
        if (bingo_board[0][column] + bingo_board[1][column] + bingo_board[2][column] + bingo_board[3][column] + bingo_board[4][column]) == 5:
            score = 1
            return score
        else:
            score = 0      
    return score

number , bingo_card, bingo_score_card = find_last_victory_board(numbers, bingo_boards_list)

for row in range(5):
    for i in range(5):
        if bingo_score_card[row][i] == 1:
            bingo_card[row][i] = 0
            
score = 0
for row in bingo_card:
    score += sum(row)
    
final_score = number * score
print('Final score is: ', final_score)