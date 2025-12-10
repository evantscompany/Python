# 문제 6.
# 2차원 좌표값은 튜플(x, y) 형태의 데이터를 사용합니다.

# point1 = (2, 3)
# point2 = (5, 7)

# 1. point1의 x좌표만 출력하시오.
# 2. point2의 y좌표만 출력하시오.

# 3. 두 좌표 간의 거리(유클리드Euclidean 거리)를 계산하시오.[ML 유사도 계산에 사용되는 거리값]
# 유클리디안 Euclidean 거리 공식:
 

point1 = (2, 3)
point2 = (5, 7)

#1.
print('point1의 x좌표 :', point1[0] )
print('point2의 y좌표 :', point2[1])


#3.
dx= (point2[0]-point1[0])**2
dy= (point2[1]-point1[1])**2
d= ( dx + dy ) ** (1/2)
print('Euclidean distance : ',  d)

