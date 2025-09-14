class Solution(object):
    def convertTemperature(self, celsius):
        ans=[]
        kelvin=celsius+273.15
        fahrenheit=(celsius*9/5)+32
        ans.append(kelvin)
        ans.append(fahrenheit)
        return ans
