class Solution:
    def isValid(self,s: str) -> bool:
        stack = []
        input_dict= {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in input_dict:  # If it's a closing bracket
              if len(stack) > 0: 
                top = stack[-1]  
                if top == input_dict[char]: 
                    stack.pop()  
                else:
                    return False 
              else:
                return False  
            else:
              stack.append(char)  # If it's an opening bracket, add it to the stack
        return len(stack) == 0
solution = Solution() 
print(solution.isValid("()")) 

