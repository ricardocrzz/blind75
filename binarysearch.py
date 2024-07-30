#initial answer
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lindex = 0
        rindex = len(nums)-1
        mindex = math.floor((rindex-lindex)/2)+lindex
        mval = nums[mindex]
        print('lindex =', lindex,'rindex =', rindex,'mindex =', mindex,'mval =', mval)

        if mval == target:
            return mindex
        elif mval > target:
            rindex = mindex - 1
        elif mval < target:
            lindex = mindex + 1
        if lindex > rindex:
            return -1
        mindex = math.floor((rindex-lindex)/2)+lindex
        mval = nums[mindex]
        print('lindex =', lindex,'rindex =', rindex,'mindex =', mindex,'mval =', mval)

        if mval == target:
            return mindex
        elif mval > target:
            rindex = mindex - 1
        elif mval < target:
            lindex = mindex + 1
        if lindex > rindex:
            return -1
        mindex = math.floor((rindex-lindex)/2)+lindex
        mval = nums[mindex]
        print('lindex =', lindex,'rindex =', rindex,'mindex =', mindex,'mval =', mval)

        if mval == target:
            return mindex
        elif mval > target:
            rindex = mindex - 1
        elif mval < target:
            lindex = mindex + 1
        if lindex > rindex:
            return -1
        mindex = math.floor((rindex-lindex)/2)+lindex
        mval = nums[mindex]
        print('lindex =', lindex,'rindex =', rindex,'mindex =', mindex,'mval =', mval)

        if mval == target:
            return mindex
        elif mval > target:
            rindex = mindex - 1
        elif mval < target:
            lindex = mindex + 1
        if lindex > rindex:
            return -1
        mindex = math.floor((rindex-lindex)/2)+lindex
        mval = nums[mindex]
        print('lindex =', lindex,'rindex =', rindex,'mindex =', mindex,'mval =', mval)

        return 99

#turn into while loop
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lindex = 0
        rindex = len(nums)-1
        mindex = math.floor((rindex-lindex)/2)+lindex
        mval = nums[mindex]
        print('lindex =', lindex,'rindex =', rindex,'mindex =', mindex,'mval =', mval)

        while lindex <= rindex:
            if mval == target:
                return mindex
            elif mval > target:
                rindex = mindex - 1
            elif mval < target:
                lindex = mindex + 1
            mindex = math.floor((rindex-lindex)/2)+lindex
            mval = nums[mindex]
            print('lindex =', lindex,'rindex =', rindex,'mindex =', mindex,'mval =', mval)
        return -1

#simplify
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = r+l //2
        mval = nums[m]
        print('lindex =', l,'rindex =', r,'mindex =', m,'mval =', mval)

        while l <= r:
            if mval == target:
                return m
            elif mval > target:
                r = m - 1
            elif mval < target:
                l = m + 1
            m = r+l //2
            mval = nums[m]
            print('lindex =', l,'rindex =', r,'mindex =', m,'mval =', mval)
        return -1