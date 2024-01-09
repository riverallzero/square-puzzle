from imagededup.methods import CNN
from PIL import Image

# CNN을 이용한 탐색
cnn_encoder = CNN()
duplicates_cnn = cnn_encoder.find_duplicates(image_dir='data', scores=True)
print(duplicates_cnn)

# 원본 이미지 순서에 맞게 번호 정렬
origin_keys = sorted([key for key in duplicates_cnn.keys() if key.startswith('origin')],
                     key=lambda x: int(x.split('_')[2].split('.')[0]))

answers = []
for key in origin_keys:
    value = duplicates_cnn[key][0][0]
    answers.append(value.split('.')[0].split('_')[-1])
print(answers)

# 정렬된 키 순서대로 이미지를 이어붙이기
result_images_row = []
current_row_images = []

for key in origin_keys:
    part_image_path = duplicates_cnn[key][0][0]
    part_image = Image.open(f'./data/{part_image_path}')

    if len(current_row_images) < 4:
        current_row_images.append(part_image)
    else:
        result_images_row.append(current_row_images)
        current_row_images = [part_image]

# 마지막 행을 결과에 추가
result_images_row.append(current_row_images)

# 각 행을 수직으로 이어붙이기
result_image = Image.new('RGB',
                         (result_images_row[0][0].width * 4, result_images_row[0][0].height * len(result_images_row)))
for i, row_images in enumerate(result_images_row):
    for j, part_image in enumerate(row_images):
        result_image.paste(part_image, (j * part_image.width, i * part_image.height))

# 결과 이미지 저장
result_image.save('result_image.jpg')
