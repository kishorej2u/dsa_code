

class Solution:
    def isValid(self, s: str) -> bool:
        try:
            print(s)
            stack = []
            for i in s:
                print(i)
                if i in "([{":
                    stack.append(i)
                        #print(f"stack is {stack}")
                    print(f"stack is {stack}")
                else:
                    if not stack:
                        return False

                    top = stack.pop()
                    if i == ')' and top!= '(':
                        return False
                    elif i == ']' and top!= '[':
                        return False
                    elif i == '}' and top!= '{':
                        return False
                return len(stack) == 0
        except Exception as e:
            print(e)
                
p1 = Solution()
print(p1.isValid("([])"))
   