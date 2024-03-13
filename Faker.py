from faker import Faker
fake = Faker(locale="zh_CN")
for i in range(20):
    print(i, fake.name())
