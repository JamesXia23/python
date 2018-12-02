class A:
	def __init__(self):
		self.x = 1
		self.a = 2
class B(A):
	pass

class C:
	pass
	
a = A()
b = B()

print(issubclass(B, A))#用于检测某个类是不是另一个类的子类（自身为自身的子类）
print(issubclass(B, B))
print(issubclass(B, (C, A)))#第二个参数可以为一个元组，只要元组中存在有一个为第一个参数的父类，则为true

print(isinstance(a, A))#用于检测某个实例对象是不是属于某个类，同样第二个参数可以为元组
try:
	print(isinstance(A, a))
except TypeError as reason:
	print('错误的原因是：' + str(reason))
	
print(hasattr(a, 'a'))#用于检测对象是否有属性

if(hasattr(a, 'x')):
	print(getattr(a, 'x'))#得到对象中的属性
else:
	print('没有这个属性')

print(getattr(a, 'y', '没有这个属性'))#设置了默认值，当对象中没有这个属性的话，就会返回默认值

if hasattr(a, 'z'):
	print('属性存在：' + str(getattr(a, 'z')))
	print('删除属性：' + str(delattr(a, 'z')))
else:
	
	print('属性不存在,正在设置属性：')