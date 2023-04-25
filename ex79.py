# Meeting rooms (how many meeting rooms are needed to organize events in given time interval?)
import heapq


class Solution(object):
    @staticmethod
    def meeting_rooms(meetings):
        meetings.sort(key=lambda x: x[0])
        meeting_ends = []
        max_rooms = 0

        for meeting in meetings:
            while meeting_ends and meeting_ends[0] <= meeting[0]:
                heapq.heappop(meeting_ends)
            heapq.heappush(meeting_ends, meeting[1])
            max_rooms = max(max_rooms, len(meeting_ends))
        return max_rooms


print(Solution.meeting_rooms([[0, 10], [10, 20]]))
# expect 1 meeting room needed

print(Solution.meeting_rooms([[20, 30], [10, 21], [0, 50]]))
# expect 3 meeting rooms needed
