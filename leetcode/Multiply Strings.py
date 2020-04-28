from collections import defaultdict

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product_map = defaultdict(int)
        for idx1, val1 in enumerate(num1[::-1]):
            for idx2, val2 in enumerate(num2[::-1]):
                product_map[idx1 + idx2]  += int(val1) * int(val2)
                print(idx1, idx2, product_map[idx1 + idx2])
                if product_map[idx1 + idx2] > 9:
                    product_map[idx1 + idx2 + 1] += product_map[idx1 + idx2] // 10
                    product_map[idx1 + idx2] %= 10
                    
        final_list = list(product_map.values())[::-1]
        for item in final_list:
            if item:
                return ''.join(map(str, final_list))
            else:
                final_list.pop(0)
                
        return "0"
