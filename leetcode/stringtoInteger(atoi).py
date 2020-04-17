class Solution:
    def myAtoi(self, str: str) -> int:
        allowed_items = dict()
        item_list = []
        nonwhite_cnt = 0
        val = 0
        s = None
        for i in "0123456789":
            allowed_items[i] = 1
        for item in str:
            if item == ' ':
                pass
            else:
                nonwhite_cnt += 1
            if item == '-' and nonwhite_cnt == 1:
                s = '-'
            elif item == '+' and nonwhite_cnt == 1:
                pass
            elif nonwhite_cnt >= 1 and item not in allowed_items and not len(item_list):
                break
            elif item not in allowed_items and len(item_list):
                break
            elif item == '.':
                break
                
            if item in allowed_items:
                item_list.append(item)
        if len(item_list):
            for idx, x in enumerate(item_list):
                val += int(x) * 10 ** (len(item_list) -idx -1)
            if s == '-':
                if -val < -2**31:
                    val = 2**31
                return -val
            else: 
                if val > 2**31-1:
                    val = 2**31-1
                return val
        else: return val
