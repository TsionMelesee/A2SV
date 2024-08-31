class Solution:
    def interpret(self, command: str) -> str:
        x = ''
        for i in range(len(command)):
            if command[i] == 'G':
                x+='G'
            elif command[i] == '(' and command[i + 1] != ')':
                x+='al'
            elif command[i] == '(' and command[i + 1] == ')':
                x+='o'
        return x


        
