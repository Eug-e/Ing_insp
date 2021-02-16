import random
from datetime import datetime
from app.models import Archive

def experiment():
	size = 1000000
	slice_size = 500
	Archive.objects.all().delete()
	for _ in range(int(size / slice_size)):
		slice = []
		for _ in range(slice_size):
			slice.append(
				Archive(
					object=str(random.randint(1,1000)),
					specialist=str(
						random.randint(10**70, 10**80)
					)
				)
			)
		Archive.objects.bulk_create(slice, slice_size)

	sum = 0
	for _ in range(100):
		start = datetime.now()
		list(Archive.objects.filter(
			credit_card_number=random.randint(
				10**70, 10**80
			)
		))
		delta = (datetime.now() - start).total_seconds()
		sum = sum + delta
print("Время выполнения 100 запросов:" + str(sum) + " секунд")