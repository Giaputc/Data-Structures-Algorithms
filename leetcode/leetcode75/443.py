class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        write=0
        read=0
        while read<n:
            curr=0
            curr_char=chars[read]
            while read<n and curr_char==chars[read]:
                curr+=1
                read+=1
            chars[write]=curr_char
            write+=1
            if curr>1:
                for i in str(curr):
                    chars[write]=i
                    write+=1
        return write