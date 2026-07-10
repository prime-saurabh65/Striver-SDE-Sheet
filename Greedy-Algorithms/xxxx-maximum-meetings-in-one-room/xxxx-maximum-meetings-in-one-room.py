# Remember: preserve original order of meetings while sorting based on
# finish time,

class Solution:
    def maxMeetings(self, s, f) :
        
        n = len(s)
        meetings = []
        for i in range(n):
            # meetings => [(satrt, end, meeting_number)]
            meetings.append((s[i], f[i], i+1))
        
        meetings.sort(key=lambda x:x[1])
        
        # print(meetings)
        last = meetings[0][1]
        
        ans = []
        first_meeting = meetings[0][2]
        ans = [first_meeting]
        
        for i in range(1, n):
            s, e, meeting = meetings[i]
            
            if s > last:
                ans.append(meeting)
                last = e
        return sorted(ans)