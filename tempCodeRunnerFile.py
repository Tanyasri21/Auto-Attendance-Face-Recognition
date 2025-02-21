new_directory = "D:/Face Recognition"
os.chdir(new_directory)


anu_image = cv2.imread("img/anu.jpg")
yugender_image = cv2.imread("img/yugender.jpg")
akhila_image = cv2.imread("img/akhila.jpg")
surya_image = cv2.imread("img/surya.jpg")
tanya_image = cv2.imread("img/tanya.jpg")

anu_encoding = face_recognition.face_encodings(anu_image)[0]
yugender_encoding = face_recognition.face_encodings(yugender_image)[0]
akhila_encoding = face_recognition.face_encodings(akhila_image)[0]
surya_encoding = face_recognition.face_encodings(surya_image)[0]
tanya_encoding = face_recognition.face_encodings(tanya_image)[0]

known_face_encoding = [
    anu_encoding,
    yugender_encoding,
    akhila_encoding,
    surya_encoding,
    tanya_encoding
]
known_faces_names = [
    "Anu",
    "Yugender",
    "Akhila",
    "Surya",
    "Tanya"
]

students = known_faces_names.copy()

video_capture = cv2.VideoCapture(0)

now = datetime.now()
current_data = now.strftime("%Y-%m-%d")


csv_file_path = current_data + '_attendance.csv'


if not os.path.isfile(csv_file_path):
    with open(csv_file_path, 'w', newline='') as f:
        lnwriter = csv.writer(f)
        lnwriter.writerow(["Name", "Time"])
