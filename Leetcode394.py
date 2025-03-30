class Solution:
    def decodeString(self, s: str) -> str:
        num_sta=[]
        str_sta=[]
        cur_num=''
        cur_str=''
        for i in range(len(s)):
            if s[i]=='[':
                str_sta.append(cur_str)
                num_sta.append(int(cur_num))
                cur_str=''
                cur_num=''
            elif s[i]==']':
                tmp=str_sta.pop()+num_sta.pop()*cur_str
                cur_str=tmp
            elif s[i].isdigit():
                cur_num+=s[i]
            else:
                cur_str+=s[i]
        return cur_str
