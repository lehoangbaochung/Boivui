from tkinter.ttk import Frame, Button
from tkinter.ttk import *
from tkinter import * 
from tkinter import Tk, Canvas, BOTH, W, Menu, ttk, Label, scrolledtext, BOTH, SUNKEN, filedialog, BooleanVar
from tkinter.colorchooser import askcolor
from datetime import date, time, datetime
import tkinter.messagebox as mbox
import tkinter as tk
import math
#định nghĩa
canchi = ['Giáp Tý','Bính Tý','Mậu Tý','Canh Tý','Nhâm Tý','Ất Sửu','Đinh Sửu','Kỷ Sửu','Tân Sửu','Quý Sửu','Bính Dần','Mậu Dần','Canh Dần','Nhâm Dần','Giáp Dần',
'Đinh Măo','Kỷ Măo','Tân Măo','Quý Măo','Ất Măo','Mậu Thìn','Canh Thìn','Nhâm Thìn','Giáp Thìn','Bính Thìn','Kỷ Tỵ','Tân Tỵ','Quý Tỵ','Ất Tỵ','Đinh Tỵ','Canh Ngọ',
'Nhâm Ngọ','Giáp Ngọ','Bính Ngọ','Mậu Ngọ','Tân Mùi','Quý Mùi','Ất Mùi','Đinh Mùi','Kỷ Mùi','Nhâm Thân','Giáp Thân','Bính Thân','Canh Thân','Mậu Thân','Quý Dậu',
'Ất Dậu','Đinh Dậu','Kỷ Dậu','Tân Dậu','Giáp Tuất','Bính Tuất','Mậu Tuất','Canh Tuất','Nhâm Tuất','Ất Hợi','Đinh Hợi','Kỷ Hợi','Tân Hợi','Quý Hợi']
can = ['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý']; chi = ['Tý','Sửu','Dần','Măo','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']
congiap = ['Chuột','Trâu','Hổ','Mèo','Rồng','Rắn','Ngựa','Dê','Khỉ','Gà','Chó','Lợn']
bq = ['Càn','Khảm','Cấn','Chấn','Tốn','Ly','Khôn','Đoài']; nh = ['Kim','Mộc','Thuỷ','Hoả','Thổ']; ngude = ['Thanh Đế','Huỳnh Đế','Bạch Đế','Xích Đế','Hắc Đế'] 
bqhh = ['Sinh khí','Phước đức','Thiên y','Phục vị','Tuyệt mệnh','Hoạ hại','Ngũ quỷ','Lục sát']
cuutrach = ['TRẠCH PHÚC', 'TRẠCH ĐỨC', 'Trạch bại', 'Trạch hư', 'Trạch khốc', 'Trạch quỷ', 'Trạch tử', 'TRẠCH BẢO', 'TRẠCH LỘC']
hoangoc = ['CUNG CÁT', 'CUNG NGHI', 'Địa Sát', 'TẤN TÀI', 'Thụ Tử', 'Hoang Ốc']
kimlau = ['Kim Lâu thân', 'Kim Lâu thê', 'Kim Lâu tử', 'Kim Lâu súc','KHÔNG PHẠM KIM LÂU']
cuudieu = ['La Hán', 'Thổ Tú', 'THUỶ DIỆU', 'Thái Bạch', 'THÁI DƯƠNG', 'Vân Hán', 'Kế Đô', 'THÁI ÂM', 'MỘC ĐỨC']
huong = ['Đông','Tây','Đông Nam','Đông Bắc','Tây Nam','Tây Bắc','Nam','Bắc']
saotot = ['Thiên đức','Nguyệt đức','Thiên giải','Thiên hỷ','Thiên quý','Tam hợp','Sinh khí','Thiên hành','Thiên quan','Lộc mã','Phúc sinh','Giải thần','Thiên ân']
saoxau = ['Thiên cương','Thụ tử','Tử khí','Quan phù','Đại hao','Tiểu hao','Sát chủ','Thiên hoả','Địa hoả','Hoả tai','Nguyệt phá','Băng tiêu ngoạ giải','Thổ cấm',
          'Thổ kỵ','Vãng vong','Cô thần','Quả tú','Trùng tang','Trùng phục']
nhithapbattu = ['Giác','Cang','Đê','Phòng','Tâm','Vĩ','Cơ','Đẩu','Ngưu','Nữ','Hư','Nguy','Thất','Bích','Khuê','Lâu','Vị','Mão','Tất','Chuỷ','Sâm','Tỉnh','Quỷ',
                'Liễu','Tinh','Trương','Dực','Chẩn']                
num=[n for n in range (1000,9999)]; numDay=[n for n in range(0,31)]; numMonth= [n for n in range(0,13)]
sao1=[10,19,28,37,46,55,64,73,82,91]; sao2=[11,20,29,38,47,56,65,74,83,92]; sao3=[12,21,30,39,48,57,66,75,84,93]; sao4=[13,22,31,40,49,58,67,76,85,94]
sao5=[14,23,32,41,50,59,68,77,86,95]; sao6=[15,24,33,42,51,60,69,78,87,96]; sao7=[16,25,34,43,52,61,70,79,88,97]; sao8=[17,26,35,44,53,62,71,80,89,98]
sao9=[18,27,36,45,54,63,72,81,90,99]
han1=[11,19,20,28,37,46,55,64,73,82,91,99]; han2=[12,21,29,30,38,47,56,65,74,83,92]; han3=[13,22,31,39,40,48,57,66,75,84,93]; han4=[14,23,32,41,49,50,58,67,76,85,94]
han5=[15,24,33,42,51,59,60,68,77,86,95]; han6=[16,25,34,43,52,61,69,70,78,87,96]; han7=[17,26,35,44,53,62,71,79,80,88,97]; han8=[10,18,27,36,45,54,63,72,81,89,90,98]
huong1m=[16,19,34,37,40,43]; huong1f=[3,12,37,45,54,57]; huong2m=[3,9,15,18,21,27,36,39,42,45,54,57]; huong2f=[19,34,40,43]; huong3=[35,38,41]
huong4=[26,29,32,44,47,50,53]; huong5m=[0,6,24,30,33,48,51]; huong5f=[1,4,7,10,22,25,28,31,46,52,55,58]; huong6m=[25,28,31,46,49,52]; huong6f=[24,30,33,39,48,49,51]
huong7m=[1,4,7,10,13,22,55,58]; huong7f=[15,18,21,27,36,42]; huong8=[2,5,8,11,14,17,20,23,56,59]
thu = ['2','3','4','5','6','7','Chủ nhật']; ngonngu = ['Tiếng Việt','English','中文简体']
ad="- Âm dương:"; ng="- Ngũ hành:"; kq="Kết quả"; tb="Thông báo"; kn="Khái niệm"; gt="Giới thiệu"; hd="Hướng dẫn"; ly="Lưu ý"; ct="Chú thích"; ds="Danh sách"
e="Lỗi nhập dữ liệu. Vui lòng nhập lại!"
#hướng dẫn
hdnhhn="Chọn mệnh ngũ hành của hai bạn cho phù hợp tại hai thanh trắng rồi sau đó nhấn nút Xác nhận. Nếu hai bạn chưa biết mệnh nguc hành \
của mình là gì, vui lòng tra tại phần \"Ngũ hành\" trong Menu chính"
hdbqhn="Chọn cung bát quái của hai bạn cho phù hợp tại hai thanh trắng rồi sau đó nhấn nút Xác nhận. Nếu hai bạn chưa biết cung bát quái \
của mình là gì, vui lòng tra tại phần \"Bát quái\" trong Menu chính"
hdtchn="Chọn thiên can của hai bạn cho phù hợp tại hai thanh trắng rồi sau đó nhấn nút Xác nhận"
hddchn="Chọn địa chi (con giáp) của hai bạn cho phù hợp tại hai thanh trắng rồi sau đó nhấn nút Xác nhận"
hdnh="Chọn mệnh ngũ hành của bạn cho phù hợp tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hdbq="Chọn cung bát quái của bạn cho phù hợp tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hdnd="*Ngũ đế hay Ngũ Thiên đế là năm vị thần trên Thiên đình trong Đạo giáo và tín ngưỡng Trung Quốc\
\n- Thuyết thứ nhất về Ngũ đế:\n+ Bắc phương: Bắc Cực Trung thiên Tử vi Đại đế\n+ Nam phương: Nam Cực Trường sinh Đại đế\
\n+ Đông phương: Đông Cực Thanh hoa Đại đế Thái Ất Cứu khổ thiên tôn\n+ Tây phương: Thái cực Thiên hoàng Đại đế\
\n+ Trung ương: Đại địa chi Mẫu, Thừa thiên Hiệu pháp Hậu thổ Hoàng địa\
\n- Thuyết thứ hai về Ngũ đế:\n+ Bắc Phương Bạch đế là Chuyên Húc\n+ Nam phương Xích đế là Thần Nông\n+ Đông phương Thanh đế là Phục Hy\
\n+ Tây phương Hắc đế là Thiếu Hạo\n+ Trung ương Huỳnh đế là Hoàng Đế\n*Ở đây ta theo thuyết thứ hai"
hdtc="Chọn thiên can của bạn cho phù hợp tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hddc="Chọn địa chi (con giáp) của bạn cho phù hợp tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hdcan="Chọn Thiên can cho phù hợp tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hdchi="Chọn Địa chi cho phù hợp tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hddl1="Nhập năm dương lịch bạn cần xem tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hddl2="Nhập ngày, tháng, năm bạn cần xem tại các thanh trắng rồi sau đó nhấn nút Xác nhận"
hdal1="Chọn năm âm lịch bạn cần xem tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hdal2="Nhập tháng âm lịch bạn cần xem tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hdas="Nhập số tuổi của bạn tại thanh trắng đầu tiên và lựa chọn giới tính của bạn rồi sau đó nhấn nút Xác nhận"
hda="Nhập độ tuổi của bạn tại thanh trắng rồi sau đó nhấn nút Xác nhận"
hds="Chọn sao bạn cần xem tại thanh trắng rồi sau đó nhấn nút Xác nhận"
ntnx="- Trước tiên cần xác định tính chất công việc, phạm vi thời gian có thể khởi công, thời gian phải hoàn thành...\n\
- Xem lịch để biết được ngày âm, ngày dương, ngày tuần lễ, ngày can chi, ngày tiết khí. Căn cứ theo ngày âm lịch có phạm ngày tam nương, nguyệt kỵ, nguyệt tận, ngày \
sóc (ngày đầu tháng) hay ngày dương công kỵ hay không?\n- Xem ngày tiết khí có phạm ngày tứ ly, tứ tuyệt hay không? (không phải mọi việc đều kiêng kỵ, ví dụ an táng, \
xây sửa mồ mả, tế tự không kỵ những ngày này).\n- Xem ngày can chi để biết được ngày trong tháng dự định công việc có những sao gì tốt, những sao gì xấu để biết tính \
chát và mức độ tốt xấu với từng việc mà quyết định. Xem ngày đó thuộc trực gì, sao gì, Hoàng đạo hay Hắc đạo?\n- Khi đã chọn được ngày tốt, phải xem ngày đó có hợp \
với bản mệnh của mình hay không (đối chiếu với ngày, tháng, năm can chi với tuổi của người chủ xem tương khắc, tương phá hay tương hợp). Đại sự như cưới hỏi, động \
thổ, khai trương, nhập trạch... phải xem kỹ. Tiểu sự chỉ tránh ngày trùng nhật (Trùng tang, trùng phục).\n- Khi xem xong ngày, muốn chắc chắn thì chọn giờ khởi sự. \
Chọn giờ chỉ chọn giờ Hoàng đạo, tránh giờ khác đi là được. Khi công việc khẩn trương không thể để nhỡ thời cơ thì phải vận dụng phép quyền biến."
#main chính
class boi(Frame):
   def __init__(self, parent):
      Frame.__init__(self, parent)  
      self.parent = parent 
      self.initUI()      
   def initUI(self):
      self.parent.title("Bói vui")
      #chọn màu nền
      self.frame = Frame(self, border=0, relief=SUNKEN, width=max, height=max)
      self.frame.place(x=0, y=0)
      #nút phải chuột
      self.menu = Menu(self.parent, tearoff=0)
      self.menu.add_command(label="Làm mới", command=self.bell())
      self.menu.add_command(label="Giới thiệu", command=self.introduce)
      self.menu.add_command(label="Kiểm tra phiên bản", command=self.update)
      self.menu.add_command(label="Thoát", command=self.master.destroy) 
      self.parent.bind("<Button-3>", self.rightKey)
      #định nghĩa menu chính
      menuBar = Menu(self.parent)
      self.parent.config(menu=menuBar)
      fileMenu1 = Menu(menuBar, tearoff=0); fileMenu2 = Menu(menuBar, tearoff=0); fileMenu3 = Menu(menuBar, tearoff=0)
      fileMenu11 = Menu(menuBar, tearoff=0); fileMenu12 = Menu(menuBar, tearoff=0); fileMenu13 = Menu(menuBar, tearoff=0); fileMenu14 = Menu(menuBar, tearoff=0)
      fileMenu15 = Menu(menuBar, tearoff=0); fileMenu16 = Menu(menuBar, tearoff=0); fileMenu17 = Menu(menuBar, tearoff=0)
      #các menu có nhánh
      submenu1 = Menu(fileMenu1, tearoff=0); submenu2 = Menu(fileMenu1, tearoff=0); submenu3 = Menu(fileMenu1, tearoff=0); submenu4 = Menu(fileMenu1, tearoff=0)
      submenu6 = Menu(fileMenu1, tearoff=0); submenu7 = Menu(fileMenu1, tearoff=0); submenu8 = Menu(fileMenu1, tearoff=0); submenu9 = Menu(fileMenu1, tearoff=0)
      submenu10 = Menu(fileMenu1, tearoff=0); submenu11 = Menu(fileMenu1, tearoff=0); submenu12 = Menu(fileMenu1, tearoff=0); submenu13 = Menu(fileMenu1, tearoff=0)
      submenu14 = Menu(fileMenu1, tearoff=0); submenu15= Menu(fileMenu1, tearoff=0); submenu16= Menu(fileMenu1, tearoff=0)
      submenu21 = Menu(fileMenu2, tearoff=0); submenu22 = Menu(fileMenu2, tearoff=0)
      submenu31 = Menu(fileMenu3, tearoff=0)
      submenu5 = Menu(fileMenu2, tearoff=0);
      #menu nhánh (1)
      fileMenu1.add_cascade(label="Hôn nhân", menu=submenu1); fileMenu1.add_cascade(label="Ngũ hành", menu=submenu2)
      fileMenu1.add_cascade(label="Bát quái", menu=submenu3); fileMenu1.add_command(label="Thiên can", command=self.thienCan)
      fileMenu1.add_cascade(label="Địa chi (con giáp)", menu=submenu4); fileMenu1.add_cascade(label="Dương lịch", menu=submenu6)
      fileMenu1.add_cascade(label="Âm lịch", menu=submenu7); fileMenu1.add_cascade(label="Ngũ đế", menu=submenu8)
      fileMenu1.add_cascade(label="Ngày tốt, ngày xấu", menu=submenu9); fileMenu1.add_cascade(label="Xem sao, xem hạn", menu=submenu10)
      fileMenu1.add_command(label="Hung niên - tam tai", command=self.hungTai); fileMenu1.add_cascade(label="Vận mệnh con người qua năm sinh", menu=submenu12)
      fileMenu1.add_cascade(label="Xây dựng nhà cửa, xuất hành", menu=submenu14)
      fileMenu1.add_cascade(label="Khai trương, xông nhà", menu=submenu15)
      fileMenu2.add_cascade(label="Cung hoàng đạo", menu=submenu5)
      #menu con cấp 2 (1)
      submenu1.add_cascade(label="Bát quái", menu=fileMenu11); submenu1.add_command(label="Ngũ hành", command=self.honNhan9)
      submenu1.add_command(label="Ngũ đế", command=self.honNhan10)                                                                                                                            
      submenu1.add_command(label="Thiên can hợp hôn", command=self.honNhan4); submenu1.add_command(label="Địa chi hợp hôn", command=self.honNhan5)
      submenu1.add_command(label="Tự kiểm tra việc hôn nhân", command=self.honNhan6); submenu1.add_cascade(label="Chọn ngày tháng tốt cho hôn nhân", menu=fileMenu12)
      submenu2.add_command(label="Tra ngũ hành", command=self.nguHanh1); submenu2.add_command(label="Sơ đồ ngũ hành", command=self.nguHanh2)
      submenu2.add_command(label="Các nguyên tắc ngũ hành", command=self.nguHanh3); submenu2.add_command(label="Bảng tương ứng ngũ hành", command=self.nguHanh4)
      submenu3.add_command(label="Tra bát quái", command=self.batQuai1)
      submenu4.add_command(label="Địa chi (con giáp)", command=self.diaChi1)
      submenu4.add_command(label="Sự tương quan giữa 12 con giáp", command=self.diaChi2)
      submenu5.add_command(label="Tra cung Hoàng đạo", command=self.hoangDao1)
      submenu6.add_command(label="Tra thứ tự ngày, tuần trong năm", command=self.duongLich1)
      submenu6.add_command(label="Tra thứ trong tuần", command=self.duongLich2)
      submenu7.add_command(label="Đổi dương lịch ra âm lịch", command=self.amLich1)
      submenu7.add_command(label="Xem ngày âm lịch", command=self.amLich2)
      submenu8.add_command(label="Tra ngũ đế", command=self.nguDe1); submenu8.add_command(label="Tính cách và vận mệnh", command=self.nguDe2)
      submenu9.add_command(label="Ngày tốt", command=self.ngayTot); submenu9.add_command(label="Ngày xấu", command=self.ngayXau)
      submenu9.add_command(label="Ngày tiết", command=self.ngayTiet); submenu9.add_command(label="Ngày trực", command=self);
      submenu9.add_command(label="Nhị thập bát tú", command=self.nhiThapBatTu); submenu9.add_command(label="Hoàng đạo, hắc đạo", command=self.hoangHac)
      submenu10.add_command(label="Tra sao, tra hạn", command=self.saoHan1); submenu10.add_command(label="Cách tiễn sao xấu và nghênh sao tốt", command=self.saoHan2)
      submenu10.add_command(label="Cửu diệu tinh (sơ đồ bày đèn cúng sao)", command=self.saoHan3)
      submenu12.add_cascade(label="Theo con giáp", menu=fileMenu16); submenu12.add_cascade(label="Theo can chi", menu=fileMenu17)
      submenu14.add_command(label="Xem tuổi xây nhà", command=self.xayDung1)
      submenu14.add_command(label="Hướng nhà", command=self.xayDung2)
      submenu15.add_command(label="Xem ngày khai trương", command=self.onWarn)
      submenu15.add_command(label="Xem tuổi xông nhà", command=self.onWarn)
      #menu con cấp 3 (1)
      fileMenu11.add_command(label="Bát quái hợp hôn", command=self.honNhan1); fileMenu11.add_command(label="Bát san giao chiến", command=self.honNhan2)
      fileMenu11.add_command(label="Bát san tuyệt mệnh", command=self.honNhan3); fileMenu12.add_command(label="Chọn ngày tốt", command=self.honNhan7)
      fileMenu12.add_command(label="Chọn tháng tốt", command=self.honNhan8)
      fileMenu16.add_command(label="Số may mắn và màu sắc", command=self.vanMenh1); fileMenu16.add_command(label="Thần tiên chiếu mệnh", command=self.onWarn)
      fileMenu16.add_command(label="Tích cách (khái quát)", command=self.onWarn); fileMenu16.add_command(label="Tình duyên, hôn nhân", command=self.onWarn)
      fileMenu16.add_command(label="Sự nghiệp, tài vận", command=self.onWarn); fileMenu16.add_command(label="Vận mệnh với các năm", command=self.onWarn)
      fileMenu16.add_command(label="Vận mệnh theo tháng sinh", command=self.onWarn); fileMenu16.add_command(label="Lựa chọn đối tác", command=self.onWarn)
      fileMenu17.add_command(label="Tính cách (chi tiết)", command=self.onWarn); fileMenu17.add_command(label="Tài vị, phúc vị", command=self.onWarn)
      #thông tin (3)
      fileMenu3.add_command(label="Giới thiệu", command=self.introduce); fileMenu3.add_command(label="Kiểm tra phiên bản", command=self.update)
      #thanh công cụ mẹ (1-2-3)
      menuBar.add_cascade(label="Phương Đông", menu=fileMenu1)
      menuBar.add_cascade(label="Phương Tây", menu=fileMenu2)
      menuBar.add_command(label="Cài đặt", command=self.settings)
      menuBar.add_cascade(label="Thông tin", menu=fileMenu3)
   #các hàm riêng
   def settings(self):
      def buttons():
         frame = Frame(self, relief=RAISED, borderwidth=1)
         frame.pack(fill=BOTH, expand=True)
         self.pack(fill=BOTH, expand=True)
         okButton = Button(self, text="OK", fg="blue")
         okButton.pack(side="left")
         closeButton = Button(self, text="Thoát", fg="red")
         closeButton.pack(side="right")
      def calendar(self):
         today = date.today()
         d = int(today.strftime("%d")); m = int(today.strftime("%m")); y = int(today.strftime("%Y"))
         cal = Calendar(window, font="Arial 14", selectmode='day', locale='en_US', cursor="hand2", year=y, month=m, day=d)
         cal.pack(fill="both", expand=True)
         def events():
            mbox.showwarning(tb, "Bạn không có sự kiện nào cả!\n"+cal.selection_get())
         ttk.Button(top, text="ok", command=events).pack()
      def color(self):
            (rgb, hx) = askcolor()
            self.frame.config(bg=hx)         
      def browse():
            file = filedialog.askopenfilename(filetypes = (("Image files","*.jpg,*.png"),("All files","*.*")))
      def colorBar():
            color(self)
            buttons()
            canvas = Canvas(self)
            canvas.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fb0")
            canvas.create_rectangle(150, 10, 240, 80, outline="#f50", fill="#f50")
            canvas.create_rectangle(270, 10, 370, 80, outline="#05f", fill="#05f")
            canvas.pack(fill=BOTH, expand=1)
      def clicked1():
            if value2.current()==0:
               calendar(self)
            elif value2.current()==1:
               color(self)
            elif value2.current()==2:
               browse()
            elif value2.current()==3:
               colorBar()               
      window = Toplevel() 
      window.title("Cài đặt") 
      window.geometry('500x200+200+200')
      display = ['Lịch','Màu sắc','Hình ảnh','Màu sắc với widgets']
      lbl = Label(window, text="Ngôn ngữ: "); lbl.grid(column=0, row=0)
      value1 = Combobox(window); value1['values']=ngonngu; value1.grid(column=1, row=0); value1.current(0)
      value2 = Combobox(window); value2['values']=display; value2.grid(column=1, row=4)
      lbl = Label(window, text=""); lbl.grid(column=0, row=1); lbl = Label(window, text=""); lbl.grid(column=0, row=3)
      lbl = Label(window, text="Âm thanh: "); lbl.grid(column=0, row=2)
      lbl = Label(window, text="Giao diện: "); lbl.grid(column=0, row=4)
      chk1_state = BooleanVar(); chk2_state = BooleanVar()
      chk1 = Checkbutton(window, text='Nền', var=chk1_state); chk1.grid(column=2, row=2)
      chk2 = Checkbutton(window, text='Thông báo', var=chk2_state); chk2.grid(column=1, row=2)
      btn = Button(window, text="Chọn", command=clicked1); btn.grid(column=2, row=4)
      window.mainloop()
   def rightKey(self, e):
      self.menu.post(e.x_root, e.y_root)
   def introduce(self):
      window = Toplevel() 
      window.title("Giới thiệu") 
      window.geometry('600x300+200+200')
      lbl = Label(window, text="* Về ứng dụng:"); lbl.grid(column=0, row=0)
      lbl = Label(window, text="- Phiên bản: 3.0.1:"); lbl.grid(column=1, row=0)
      lbl = Label(window, text="Phát hành bản vá ngày 27/7/2019"); lbl.grid(column=2, row=0)
      lbl = Label(window, text="- Nguồn ứng dụng: "); lbl.grid(column=1, row=1)
      lbl = Label(window, text="12 con giáp, tính cách con người qua năm sinh\n(NXB Mỹ thuật, in quý III năm 2010)"); lbl.grid(column=2, row=1)
      lbl = Label(window, text="* Về tác giả:"); lbl.grid(column=0, row=2)
      lbl = Label(window, text="Lê Hoàng Bảo Chung (#ZH):"); lbl.grid(column=1, row=2)
      lbl = Label(window, text="- Facebook: Chung Chung\n- Youtube: Zither Harp\n- Email: lehoangbaochung@gmail.com"); lbl.grid(column=2, row=2)
   def update(self):
      def check():
         pb = ttk.Progressbar(window, orient='horizontal', length=200, mode='determinate')
         pb.grid(column=1, row=1)
         pb.start(0); 
         lbl = Label(window, text="Tiến trình: "); lbl.grid(column=0, row=1)
         mbox.showwarning(tb, "Không phát hiện bản cập nhật mới!")         
         lbl = Label(window, text="Không có bản cập nhật mới"); lbl.grid(column=1, row=2)
         pb.stop()
         lbl = Label(window, text="Trạng thái: "); lbl.grid(column=0, row=2)
         lbl = Label(window, text="Đã xong"); lbl.grid(column=2, row=1)
         btn = Button(window, text="Kiểm tra", command=check); btn.grid(column=2, row=2)
      window = Toplevel()
      window.title("Kiểm tra phiên bản") 
      window.geometry('500x150+100+200')
      lbl = Label(window, text="Phiên bản hiện tại: "); lbl.grid(column=0, row=0);
      lbl = Label(window, text="v3.0.1 (cập nhật ngày 27/7/2019)"); lbl.grid(column=1, row=0)
      lbl = Label(window, text="Cập nhật: "); lbl.grid(column=0, row=1)
      btn = Button(window, text="Kiểm tra", command=check); btn.grid(column=2, row=1)      
      window.mainloop()
   #thân chương trình
   def honNhan1(self):
      def info():
         mbox.showwarning(gt, "Bát quái hợp hôn là sự phối hợp của các cung kí sinh (hay còn gọi là bát quái): "+str(bq)+\
                              " sẽ cho ra kết quả của cuộc hôn nhân như sau")
      def help():
         mbox.showwarning(hd, hdbqhn)
      def clicked():
         if gt1.current()<0 or gt2.current()<0 or gt1.current()>7 or gt2.current()>7:
            mbox.showerror("Lỗi",e)
         elif gt1.current()==0 and gt2.current()==7 or gt1.current()==1 and gt2.current()==4 or gt1.current()==2 and gt2.current()==6\
            or gt1.current()==3 and gt2.current()==5 or gt1.current()==4 and gt2.current()==1 or gt1.current()==6 and gt2.current()==2\
            or gt1.current()==5 and gt2.current()==3 or gt1.current()==7 and gt2.current()==0:
            mbox.showinfo(kq,"Sinh khí: rất tốt")
         elif gt1.current()==0 and gt2.current()==6 or gt1.current()==6 and gt2.current()==0 or gt1.current()==1 and gt2.current()==5\
            or gt1.current()==5 and gt2.current()==1 or gt1.current()==2 and gt2.current()==7 or gt1.current()==7 and gt2.current()==2\
            or gt1.current()==3 and gt2.current()==4 or gt1.current()==4 and gt2.current()==3:
            mbox.showinfo(kq,"Phước đức: tốt, tuy có xung khắc")
         elif gt1.current()==0 and gt2.current()==2 or gt1.current()==2 and gt2.current()==0 or gt1.current()==1 and gt2.current()==3\
            or gt1.current()==3 and gt2.current()==1 or gt1.current()==gt2.current()==4 or gt1.current()==gt2.current()==5\
            or gt1.current()==6 and gt2.current()==7 or gt1.current()==7 and gt2.current()==6:
            mbox.showinfo(kq,"Thiên y: mệnh vợ làm chủ tiền tài")       
         elif gt1.current()==gt2.current()==0 or gt1.current()==gt2.current()==1 or gt1.current()==gt2.current()==2 or gt1.current()==gt2.current()==3\
            or gt1.current()==gt2.current()==5 or gt1.current()==gt2.current()==6 or gt1.current()==gt2.current()==7 or gt1.current()==4 and gt2.current()==5:
            mbox.showinfo(kq,"Phục vị: đôi khi dễ xảy ra việc khắc khẩu, con cháu thành đạt trung bình")
         elif gt1.current()==0 and gt2.current()==5 or gt1.current()==1 and gt2.current()==6 or gt1.current()==2 and gt2.current()==4\
            or gt1.current()==3 and gt2.current()==7 or gt1.current()==4 and gt2.current()==2 or gt1.current()==5 and gt2.current()==0\
            or gt1.current()==6 and gt2.current()==1 or gt1.current()==7 and gt2.current()==3:
            mbox.showinfo(kq,"Tuyệt mệnh: chồng chết sớm hoặc vợ bệnh nặng lúc hậu sản")
         elif gt1.current()==0 and gt2.current()==4 or gt1.current()==4 and gt2.current()==0 or gt1.current()==1 and gt2.current()==7\
            or gt1.current()==7 and gt2.current()==1 or gt1.current()==2 and gt2.current()==5 or gt1.current()==5 and gt2.current()==2\
            or gt1.current()==6 and gt2.current()==3 or gt1.current()==3 and gt2.current()==6:
            mbox.showinfo(kq,"Hoạ hại: khắc khẩu bất hoà")
         elif gt1.current()==0 and gt2.current()==3 or gt1.current()==3 and gt2.current()==0 or gt1.current()==1 and gt2.current()==2\
            or gt1.current()==2 and gt2.current()==1 or gt1.current()==4 and gt2.current()==6 or gt1.current()==6 and gt2.current()==4\
            or gt1.current()==5 and gt2.current()==7 or gt1.current()==7 and gt2.current()==5:
            mbox.showinfo(kq,"Ngũ quỷ: dễ sinh ly tử biệt")
         else:
            mbox.showinfo(kq,"Lục sát: chăn nuôi không đạt")
      info()     
      window = Toplevel()
      window.title("Bát quái hợp hôn") 
      window.geometry('700x50+100+200')
      lbl = Label(window, text="Cung bát quái của nam:"); lbl.grid(column=0, row=0)
      lbl = Label(window, text="Cung bát quái của nữ:"); lbl.grid(column=2, row=0)
      gt1 = Combobox(window); gt1['values']=bq; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=bq; gt2.grid(column=3, row=0)      
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=4, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def honNhan2(self):
      def info():
         mbox.showwarning(gt, "Bát san giao chiến là sự khắc khẩu bất hoà, xung đột triền miên, khi các cung Bát quái phối hợp với nhau")
      def help():
         mbox.showwarning(hd, hdbqhn)
      def clicked():
         if gt1.current()==0 and gt2.current()==4 or gt1.current()==4 and gt2.current()==0 or gt1.current()==0 and gt2.current()==6\
            or gt1.current()==6 and gt2.current()==0 or gt1.current()==2 and gt2.current()==6 or gt1.current()==6 and gt2.current()==2\
            or gt1.current()==6 and gt2.current()==3 or gt1.current()==3 and gt2.current()==6 or gt1.current()==5 and gt2.current()==7\
            or gt1.current()==7 and gt2.current()==5 or gt1.current()==3 and gt2.current()==4 or gt1.current()==4 and gt2.current()==3\
            or gt1.current()==5 and gt2.current()==6 or gt1.current()==6 and gt2.current()==5 or gt1.current()==1 and gt2.current()==5\
            or gt1.current()==5 and gt2.current()==1:
            mbox.showinfo(kq,"Cung bát quái của hai bạn tạo thành một cặp bát san giao chiến!")
         elif gt1.current()<0 or gt2.current()<0 or gt1.current()>7 or gt2.current()>7:
            mbox.showerror("Lỗi",e)
         else:
            mbox.showinfo(kq,"Cung bát quái của hai bạn không tạo thành một cặp bát san giao chiến!")
      info()
      window = Toplevel() 
      window.title("Bát quái giao chiến") 
      window.geometry('700x50+100+200')
      lbl = Label(window, text="Cung bát quái của nam:"); lbl.grid(column=0, row=0)
      lbl = Label(window, text="Cung bát quái của nữ:"); lbl.grid(column=2, row=0)
      gt1 = Combobox(window); gt1['values']=bq; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=bq; gt2.grid(column=3, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=4, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)      
      window.mainloop()    
   def honNhan3(self):
      def info():
         mbox.showwarning(hd, "Bát san giao chiến là những cặp xấu nhất, mệnh người này triệt người kia, nhưng tất cả không có nghĩa là một trong hai sẽ tử biệt.\
Tuỳ theo mức xung khắc, nếu nhẹ thì dẫn đến khắc khẩu bất hoà, nặng thì con cái bệnh tật, hư hỏng và là nguyên nhân dẫn đến sự nghèo túng cơ cực.")
      def help():
         mbox.showwarning(hd, hdbqhn)
      def clicked():
         if gt1.current()==0 and gt2.current()==5 or gt1.current()==5 and gt2.current()==0 or gt1.current()==2 and gt2.current()==4\
            or gt1.current()==4 and gt2.current()==2 or gt1.current()==1 and gt2.current()==6 or gt1.current()==6 and gt2.current()==1\
            or gt1.current()==3 and gt2.current()==7 or gt1.current()==7 and gt2.current()==3:
            mbox.showinfo(kq,"Cung bát quái của hai bạn tạo thành một cặp bát san tuyệt mệnh!")
         elif gt1.current()<0 or gt2.current()<0 or gt1.current()>7 or gt2.current()>7:
            mbox.showerror("Lỗi",e)
         else:
            mbox.showinfo(kq,"Cung bát quái của hai bạn không tạo thành một cặp bát san tuyệt mệnh!")
      info()
      window = Toplevel() 
      window.title("Bát quái giao chiến") 
      window.geometry('700x50+200+200')
      lbl = Label(window, text="Cung bát quái của nam:"); lbl.grid(column=0, row=0)
      lbl = Label(window, text="Cung bát quái của nữ:"); lbl.grid(column=2, row=0)
      gt1 = Combobox(window); gt1['values']=bq; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=bq; gt2.grid(column=3, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=4, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
      print("*Chú ý: đây là cặp xấu nhất, tuy nhiên nếu các can chi mệnh phù hợp thì độ nguy hại giảm thiểu rõ rệt.\
\nNhưng cũng đừng vì sự tương khắc ấy mà những người yêu nhau quá sợ hăi!")
      print("-"*50)   
   def honNhan4(self):
      def info():
         mbox.showwarning(gt, "Thiên can hợp hôn là kết quả của hai thiên can khi phối hợp với nhau")
      def help():
         mbox.showwarning(hd, hdtchn)
      def clicked():
         if gt1.current()<0 or gt2.current()<0 or gt1.current()>7 or gt2.current()>7:
            mbox.showerror("Lỗi",e)
         elif gt1.current()==0 and gt2.current()==5 or gt1.current()==5 and gt2.current()==0 or gt1.current()==1 and gt2.current()==6\
            or gt1.current()==6 and gt2.current()==1 or gt1.current()==2 and gt2.current()==7 or gt1.current()==7 and gt2.current()==2\
            or gt1.current()==3 and gt2.current()==8 or gt1.current()==8 and gt2.current()==3 or gt1.current()==4 and gt2.current()==9\
            or gt1.current()==9 and gt2.current()==4:
            mbox.showinfo(kq,"Thiên can của hai bạn hợp nhau!")
         elif gt1.current()==0 and gt2.current()==4 or gt1.current()==4 and gt2.current()==0 or gt1.current()==1 and gt2.current()==5\
            or gt1.current()==5 and gt2.current()==1 or gt1.current()==2 and gt2.current()==6 or gt1.current()==6 and gt2.current()==2\
            or gt1.current()==3 and gt2.current()==7 or gt1.current()==7 and gt2.current()==3 or gt1.current()==4 and gt2.current()==8\
            or gt1.current()==8 and gt2.current()==4:
            mbox.showinfo(kq,"Thiên can của hai bạn phá nhau!")
         elif gt1.current()==0 and gt2.current()==6 or gt1.current()==6 and gt2.current()==0 or gt1.current()==1 and gt2.current()==7\
            or gt1.current()==7 and gt2.current()==1 or gt1.current()==2 and gt2.current()==8 or gt1.current()==8 and gt2.current()==2\
            or gt1.current()==3 and gt2.current()==9 or gt1.current()==9 and gt2.current()==3 or gt1.current()==4 and gt2.current()==0\
            or gt1.current()==0 and gt2.current()==4:
            mbox.showinfo(kq,"Thiên can của hai bạn xung khắc nhau!")
         else:
            mbox.showinfo(kq,"Thiên can của hai bạn bình thường!")
      window = Toplevel() 
      window.title("Thiên can hợp hôn") 
      window.geometry('700x50+100+200')
      lbl = Label(window, text="Thiên can của nam:"); lbl.grid(column=0, row=0); lbl = Label(window, text="Thiên can của nữ:"); lbl.grid(column=2, row=0)        
      gt1 = Combobox(window); gt1['values']=can; gt1.grid(column=1, row=0); gt2 = Combobox(window); gt2['values']=can; gt2.grid(column=3, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=0, row=4)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop() 
   def honNhan5(self):
      def info():
         mbox.showwarning(gt, "Địa chi hợp hôn là kết quả của hai địa chi (con giáp) khi phối hợp với nhau")
      def help():
         mbox.showwarning(hd, hddchn)
      def clicked():
         if gt1.current()==0 and gt2.current()==1 or gt1.current()==1 and gt2.current()==0 or gt1.current()==2 and gt2.current()==11\
            or gt1.current()==11 and gt2.current()==2 or gt1.current()==3 and gt2.current()==10 or gt1.current()==10 and gt2.current()==3\
            or gt1.current()==4 and gt2.current()==9 or gt1.current()==9 and gt2.current()==4 or gt1.current()==5 and gt2.current()==8\
            or gt1.current()==8 and gt2.current()==5 or gt1.current()==6 and gt2.current()==7 or gt1.current()==7 and gt2.current()==6:
            mbox.showinfo(kq,"Địa chi của hai bạn hợp nhau!")
         elif gt1.current()<0 or gt2.current()<0 or gt1.current()>7 or gt2.current()>7:
            mbox.showerror("Lỗi",e)
         else:
            mbox.showinfo(kq,"Địa chi của hai bạn bình thường!")
      window = Toplevel() 
      window.title("Địa chi hợp hôn") 
      window.geometry('700x50+100+200')
      lbl = Label(window, text="Địa chi của nam:"); lbl.grid(column=0, row=0)
      lbl = Label(window, text="Địa chi của nữ:"); lbl.grid(column=2, row=0)
      gt1 = Combobox(window); gt1['values']=chi; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=chi; gt2.grid(column=3, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=4, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()     
   def honNhan6(self):
      def info():
         mbox.showwarning(gt, "Một số nhà toán học am hiểu và có chuyên môn đã đưa ra thang điểm (thang 100đ) cho việc hôn nhân, cưới hỏi như sau: \n\
- Tình yêu, sự hoà hợp: +50đ\n- Ngũ hành hợp hôn: +12.5đ\n- Bát quái hợp hôn: +12.5đ\n- Thiên can hợp hôn: +12.5đ\n- Địa chi hợp hôn: +12.5đ\
\n- Bát san giao chiến: -15đ\n- Bát san tuyệt mệnh: -20đ")
      def help():
         mbox.showwarning(hd, "- Chọn thông tin của hai bạn cho phù hợp tại các thanh trắng rồi sau đó nhấn nút Xác nhận. Nếu hai bạn chưa rõ các thông tin \
của mình là gì, vui lòng tra các phần chưa biết còn thiếu tại các phần trong Menu chính\n\
- Khi đã điền xong tất cả thông tin, hãy nhấn nút Tổng điểm để xem kết quả!")
      info()
      def clicked():
         count=sum1+sum2+sum3+sum4+sum5+sum6
         if count<101 and count>=0 and sum1<51 and sum1>=0:
            if count<101 and count>94:
               mbox.showinfo("Kết quả", "Đánh giá: S (Lí tưởng)\nXin chúc mừng! Hai bạn đă đạt được số điểm tốt nhất! Hai bạn là một cặp đôi lí tưởng!")
            elif count<95 and count>74:
               mbox.showinfo("Kết quả", "Đánh giá: A (Tốt)")
            elif count<75 and count>54:
               mbox.showinfo("Kết quả", "Đánh giá: B (Khá)")
            elif count<55 and count>44:
               mbox.showinfo("Kết quả", "Đánh giá: C (Trung bình)\nHai bạn chỉ có tình yêu, sự hoà hợp hoặc chỉ có các yếu tố siêu hình")
            elif count<45 and count>39:
               mbox.showinfo("Kết quả", "Đánh giá: D\n=> Dễ phiêu lưu trong việc hôn nhân")
            elif count<40 and count>24:
               mbox.showinfo("Kết quả", "Đánh giá: E\n=> Hạnh phúc bị nhiều yếu tố đe doạ")
            elif count<25 and count>=0:
               mbox.showinfo("Kết quả", "Đánh giá: F\n=> Hạnh phúc luôn bên bờ vực")
         else:
            mbox.showerror("Lỗi","Oops! Đă xảy ra lỗi trong quá trình nhập dữ liệu")
      def clicked1():
         global sum1; sum1=count1=int(spin.get())
         if count1<0 or count1>50:
            mbox.showerror("Lỗi",e)
         else:
            lbl13.configure(text="+ %d điểm" %(count1))
      def clicked2():
         global sum2; x=value1.current(); y=value2.current(); count2=0
         if (x==0 and y==2) or (x==0 and y==4):
            sum2=count2=12.5
            lbl24.configure(text="+ %d điểm" %(count2))            
         elif x==y==0:
            if messagebox.askyesno("Xác nhận","Hai bạn mạng Kim có giống nhau không (ví dụ: cùng là Thoa Xuyến Kim) ?"):
               sum2=count2=6.25
               lbl24.configure(text="+ %d điểm" %(count2))
            else:
               sum2=count2=0
               lbl24.configure(text="+ %d điểm" %(count2))
         elif (x==0 and y==1) or (x==0 and y==3):
            sum2=count2=0
            lbl24.configure(text="+ %d điểm" %(count2))
         elif (x==1 and y==2) or (x==1 and y==3):
            sum2=count2=12.5
            lbl24.configure(text="+ %d điểm" %(count2))
         elif (x==1 and y==4) or (x==1 and y==1):
            sum2=count2=6.25
            lbl24.configure(text="+ %d điểm" %(count2))
         elif x==1 and y==0:
            sum2=count2=0
            lbl24.configure(text="+ %d điểm" %(count2))
         elif (x==2 and y==0) or (x==2 and y==1):
            sum2=count2=12.5
            lbl24.configure(text="+ %d điểm" %(count2))
         elif x==y==2:
            if messagebox.askyesno("Xác nhận","Hai bạn mạng Thuỷ có giống nhau không (ví dụ: cùng là Trường Lưu Thuỷ) ?"):
               sum2=count2=6.25
               lbl24.configure(text="+ %d điểm" %(count2))
            else:
               sum2=count2=0
               lbl24.configure(text="+ %d điểm" %(count2))
         elif x==2 and y==3:
            sum2=count2=6.25
            lbl24.configure(text="+ %d điểm" %(count2))
         elif x==2 and y==4:
            sum2=count2=0
            lbl24.configure(text="+ %d điểm" %(count2))
         elif (x==3 and y==1) or (x==3 and y==4):
            sum2=count2=12.5
            lbl24.configure(text="+ %d điểm" %(count2))
         elif x==y==3:
            sum2=count2=6.25
            lbl24.configure(text="+ %d điểm" %(count2))
         elif x==3 and y==0 or x==3 and y==2:
            sum2=count2=0
            lbl24.configure(text="+ %d điểm" %(count2))
         elif (x==4 and y==0) or (x==4 and y==3):
            sum2=count2=12.5
            lbl24.configure(text="+ %d điểm" %(count2))
         elif x==y==4:
            sum2=count2=6.25
            lbl24.configure(text="+ %d điểm" %(count2))
         elif (x==4 and y==1) or (x==4 and y==2):
            sum2=count2=0
            lbl24.configure(text="+ %d điểm" %(count2))
         else:
            sum2=0
            mbox.showerror("Lỗi",e)  
      def clicked3():
         global sum3; x=value3.current(); count3=0
         if x==0:
            sum3=count3=6.25
            lbl33.configure(text="+ %d điểm" %(count3))
         elif x==1:
            sum3=count3=10.9375
            lbl33.configure(text="+ %d điểm" %(count3))
         elif x==2:
            sum3=count3=9.375
            lbl33.configure(text="+ %d điểm" %(count3))
         elif x==3:
            sum3=count3=7.8125
            lbl33.configure(text="+ %d điểm" %(count3))
         elif x==7:
            sum3=count3=6.25
            lbl33.configure(text="+ %d điểm" %(count3))
         elif x==6:
            sum3=count3=4.6875
            lbl33.configure(text="+ %d điểm" %(count3))
         elif x==5:
            sum3=count3=3.125
            lbl33.configure(text="+ %d điểm" %(count3))
         elif x==4:
            sum3=count3=1.5625
            lbl33.configure(text="+ %d điểm" %(count3))
         else:
            sum3=0
            mbox.showerror("Lỗi",e)
      def clicked4():
         global sum4; x=value4.current(); y=value5.current(); count4=0
         if x<0 or y<0 or x>9 or y>9:
            mbox.showerror("Lỗi",e)
         elif (x==0 and y==5) or (x==1 and y==6) or (x==2 and y==7) or (x==3 and y==8) or (x==4 and y==9) or (x==5 and y==0) or (x==6 and y==1) or (x==7 and y==2)\
            or (x==8 and y==3) or (x==9 and y==4):
            sum4=count4=12.5
            lbl44.configure(text="+ %d điểm" %(count4))
         elif (x==0 and y==4) or (x==1 and y==5) or (x==2 and y==6) or (x==3 and y==7) or (x==4 and y==8) or (x==5 and y==9) or (x==6 and y==0) or (x==7 and y==1)\
            or (x==8 and y==2) or (x==9 and y==3):
            sum4=count4=6.25
            lbl44.configure(text="+ %d điểm" %(count4))
         elif (x==0 and y==6) or (x==1 and y==7) or (x==2 and y==8) or (x==3 and y==9) or (x==4 and y==0) or (x==5 and y==1) or (x==6 and y==2) or (x==7 and y==3)\
            or (x==8 and y==4) or (x==9 and y==5):
            sum4=count4=3.125
            lbl44.configure(text="+ %d điểm" %(count4))
         else:
            sum4=count4=9.375
            lbl44.configure(text="+ %d điểm" %(count4))
      def clicked5():
         global sum5; x=value6.current(); y=value7.current(); count5=0
         if x<0 or y<0 or x>11 or y>11:
            mbox.showerror("Lỗi",e)
         elif (x==0 and y==1) or (x==1 and y==0) or (x==2 and y==11) or (x==11 and y==2) or (x==3 and y==10) or (x==10 and y==3) or (x==4 and y==9)\
            or (x==9 and y==4) or (x==5 and y==8) or (x==8 and y==5) or (x==6 and y==7) or (x==7 and x==6):
            sum5=count5=12.5
            lbl54.configure(text="+ %d điểm" %(count5))
         else:
            sum5=count5=6.25
            lbl54.configure(text="+ %d điểm" %(count5))
      def clicked6():
         global sum6; x=value8.current(); y=value9.current(); count6=0
         if x<0 or y<0 or x>7 or y>7:
            mbox.showerror("Lỗi",e)
         elif (x==0 and y==4) or (x==4 and y==0) or (x==0 and y==6) or (x==6 and y==0) or (x==6 and y==2) or (x==2 and y==6) or (x==6 and y==3)\
            or (x==3 and y==6) or (x==7 and y==5) or (x==5 and y==7) or (x==3 and y==4) or (x==4 and y==3) or (x==5 and y==6) or (x==6 and y==5)\
            or (x==1 and y==5) or (x==5 and y==1):
            mbox.showarning(tb,"Cung bát quái "+x+" và cung bát quái "+y+" tạo thành một cặp bát san giao chiến !")
            sum6=count6=-15
            lbl64.configure(text=" %d điểm" %(count6))
         elif (x==0 and y==5) or (x==5 and y==0) or (x==2 and y==4) or (x==4 and y==2) or (x==1 and y==6) or (x==6 and y==1)\
              or (x==3 and y==7) or (x==7 and y==3):
            mbox.showwarning(tb,"Cung bát quái "+bq[x]+" và cung bát quái "+bq[y]+" tạo thành một cặp bát san tuyệt mệnh !")
            sum6=count6=-20
            lbl64.configure(text=" %d điểm" %(count6))
         else:
            sum6=0
            mbox.showwarning(tb,"Chúc mừng! Hai cung bát quái "+bq[x]+" và "+bq[y]+" của hai bạn không phải là một cặp bát san giao chiến hoặc bát san tuỵệt mệnh!")
            lbl64.configure(text="- %d điểm" %(count6))
      window = Toplevel() 
      window.title("Tự kiểm tra việc hôn nhân") 
      window.geometry('900x350+50+100')
      lbl11 = Label(window, text="*Tình yêu, sự hoà hợp: "); lbl11.grid(column=0, row=0); lbl12 = Label(window, text=""); lbl12.grid(column=1, row=0)
      lbl12 = Label(window, text="(tự đánh giá: 0-50)"); lbl12.grid(column=2, row=0); lbl13 = Label(window, text=""); lbl13.grid(column=6, row=0)
      spin = Spinbox(window, fg="blue", font=12, from_=0, to=50, width=14); spin.grid(column=3,row=0); lbl = Label(window, text=""); lbl.grid(column=0, row=1)
      lbl31 = Label(window, text="*Bát quái hợp hôn:"); lbl31.grid(column=0, row=3); lbl33 = Label(window, text=""); lbl33.grid(column=6, row=3)
      lbl32 = Label(window, text="Quẻ bát quái của hai bạn: "); lbl32.grid(column=2, row=3)
      value3 = Combobox(window); value3['values']=bqhh; value3.grid(column=3, row=3);  lbl = Label(window, text=""); lbl.grid(column=0, row=4)
      lbl21 = Label(window, text="*Ngũ hành hợp hôn:"); lbl21.grid(column=0, row=5); lbl24 = Label(window, text=""); lbl24.grid(column=6, row=5)
      lbl22 = Label(window, text="Ngũ hành của nam: "); lbl22.grid(column=1, row=5); lbl23 = Label(window, text="Ngũ hành của nữ: "); lbl23.grid(column=3, row=5)      
      value1 = Combobox(window); value1['values']=nh; value1.grid(column=2, row=5); value2 = Combobox(window); value2['values']=nh; value2.grid(column=4, row=5)
      lbl = Label(window, text=""); lbl.grid(column=0, row=6)
      lbl41 = Label(window, text="*Thiên can hợp hôn:"); lbl41.grid(column=0, row=7); lbl44 = Label(window, text=""); lbl44.grid(column=6, row=7)
      lbl42 = Label(window, text="Thiên can của nam: "); lbl42.grid(column=1, row=7); lbl43 = Label(window, text="Thiên can của nữ: "); lbl43.grid(column=3, row=7)
      value4 = Combobox(window); value4['values']=can; value4.grid(column=2, row=7); value5 = Combobox(window); value5['values']=can; value5.grid(column=4, row=7)
      lbl = Label(window, text=""); lbl.grid(column=0, row=8)
      lbl51 = Label(window, text="*Địa chi hợp hôn:"); lbl51.grid(column=0, row=9); lbl54 = Label(window, text=""); lbl54.grid(column=6, row=9)
      lbl52 = Label(window, text="Địa chi của nam: "); lbl52.grid(column=1, row=9); lbl53 = Label(window, text="Địa chi của nữ: "); lbl53.grid(column=3, row=9)
      value6 = Combobox(window); value6['values']=chi; value6.grid(column=2, row=9); value7 = Combobox(window); value7['values']=chi; value7.grid(column=4, row=9)
      lbl = Label(window, text=""); lbl.grid(column=0, row=10); lbl61 = Label(window, text="*Bát san giao chiến\n& tuyệt mệnh:"); lbl61.grid(column=0, row=11)
      lbl64 = Label(window, text=""); lbl64.grid(column=6, row=11)
      lbl62 = Label(window, text="Bát quái của nam: "); lbl62.grid(column=1, row=11); lbl63 = Label(window, text="Bát quái của nữ: "); lbl63.grid(column=3, row=11)
      value8 = Combobox(window); value8['values']=bq; value8.grid(column=2, row=11); value9 = Combobox(window); value9['values']=bq; value9.grid(column=4, row=11)
      lbl71 = Label(window, text=""); lbl71.grid(column=0, row=12)
      btn1 = Button(window, text="Xác nhận", command=clicked1); btn1.grid(column=5, row=0)
      btn2 = Button(window, text="Xác nhận", command=clicked3); btn2.grid(column=5, row=3)
      btn3 = Button(window, text="Xác nhận", command=clicked2); btn3.grid(column=5, row=5)      
      btn4 = Button(window, text="Xác nhận", command=clicked4); btn4.grid(column=5, row=7)
      btn5 = Button(window, text="Xác nhận", command=clicked5); btn5.grid(column=5, row=9)
      btn6 = Button(window, text="Xác nhận", command=clicked6); btn6.grid(column=5, row=11)
      btn7 = Button(window, text="Tổng điểm", command=clicked); btn7.grid(column=3, row=13)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def honNhan7(self):
      def info():
         mbox.showwarning(gt, "Xem ngày tốt, xấu trong hôn nhân")
      def help():
         mbox.showwarning(hd, hdal2)
      def clicked1():
         x = int(spin1.get())
         if x==1:
            mbox.showinfo(kq, "Ngày: Tân Hợi, Tân Sửu, Tân Mão, Canh Tý, Kỷ Hợi, Kỷ Sửu, Kỷ Mão, Đinh Sửu, Đinh Hợi, Đinh Mão, Bính Tý, Bính Dần")
         elif x==2:
            mbox.showinfo(kq, "Ngày: Canh Tý, Canh Dần, Canh Tuất, Kỷ Hợi, Kỷ Sửu, Đinh Hợi, Đinh Sửu, Bính Tuất, Bính Tý, Bính Dần, Ất Hợi, Ất Sửu")
         elif x==3:
            mbox.showinfo(kq, "Ngày: Kỷ Dậu, Kỷ Hợi, Kỷ Sửu, Đinh Hợi, Đinh Dậu, Đinh Sửu, Bính Tuất, Bính Tý, Ất Hợi, Ất Sửu, Giáp Tuất, Giáp Tý")
         elif x==4:
            mbox.showinfo(kq, "Ngày: Đinh Dậu, Đinh Hợi, Bính Thân, Bính Tuất, Bính Tý, Ất Dậu, Ất Hợi, Giáp Thân, Giáp Tuất, Giáp Tý, Mậu Thân, Mậu Tý, Mậu Tuất")
         elif x==5:
            mbox.showinfo(kq, "Ngày: Bính Thân, Bính Tuất, Ất Mùi, Ất Hợi, Ất Dậu, Giáp Thân, Giáp Tuất, Mậu Thân, Mậu Tuất, Quý Mùi, Quý Dậu, Quý Hợi")
         elif x==6:
            mbox.showinfo(kq, "Ngày: Ất Mùi, Ất Dậu, Giáp Ngọ, Giáp Thân, Mậu Ngọ, Giáp Tuất, Mậu Tuất, Quý Mùi, Quý Dậu, Nhâm Ngọ, Nhâm Thân, Nhâm Tuất")
         elif x==7:
            mbox.showinfo(kq, "Ngày: Ất Tỵ, Ất Mùi, Ất Dậu, Giáp Ngọ, Giáp Thân, Mậu Ngọ, Mậu Thân, Quý Tỵ, Quý Mùi, Quý Dậu, Nhâm Ngọ, Nhâm Thân")
         elif x==8:
            mbox.showinfo(kq, "Ngày: Giáp Thìn, Giáp Ngọ, Giáp Thân, Mậu Thìn, Mậu Ngọ, Mậu Thân, Quý Tỵ, Quý Mùi, Nhâm Thìn, Nhâm Thân, Nhâm Ngọ, Tân Tỵ, Tân Mùi, \
Canh Thìn, Canh Ngọ")
         elif x==9:
            mbox.showinfo(kq, "Ngày: Mậu Thìn, Mậu Ngọ, Quý Mão, Quý Tỵ, Quý Mùi, Nhâm Thìn, Nhâm Ngọ, Tân Mão, Tân Tỵ, Tân Mùi, Canh Thìn, Canh Ngọ")
         elif x==10:
            mbox.showinfo(kq, "Ngày: Quý Mão, Quý Tỵ, Nhâm Thìn, Nhâm Ngọ, Tân Mão, Tân Tỵ, Canh Thìn, Canh Ngọ, Canh Dần, Kỷ Mão, Kỷ Tỵ")
         elif x==11:
            mbox.showinfo(kq, "Ngày: Nhâm Dần, Nhâm Thìn, Tân Sửu, Tân Mão, Tân Tỵ, Canh Dần, Canh Thìn, Kỷ Sửu, Kỷ Mão, Kỷ Tỵ, Đinh Sửu, Đinh Mão, Đinh Tỵ")
         elif x==12:
            mbox.showinfo(kq, "Ngày: Tân Sửu, Tân Mão, Canh Tý, Canh Dần, Canh Thìn, Kỷ Sửu, Kỷ Mão, Đinh Sửu, Đinh Mão, Bính Tý, Bính Dần, Bính Thìn")
         else:
            mbox.showerror("Lỗi",e)        
      def clicked2():
         x = int(spin2.get())
         if x==1:
            mbox.showinfo(kq, "Ngày Thìn")
         elif x==2:
            mbox.showinfo(kq, "Ngày Sửu")
         elif x==3:
            mbox.showinfo(kq, "Ngày Mùi")
         elif x==4:
            mbox.showinfo(kq, "Ngày Tý")
         elif x==5:
            mbox.showinfo(kq, "Ngày Mão")
         elif x==6:
            mbox.showinfo(kq, "Ngày Hợi")
         elif x==7:
            mbox.showinfo(kq, "Ngày Tuất")
         elif x==8:
            mbox.showinfo(kq, "Ngày Tỵ")
         elif x==9:
            mbox.showinfo(kq, "Ngày Dần")
         elif x==10:
            mbox.showinfo(kq, "Ngày Thân")
         elif x==11:
            mbox.showinfo(kq, "Ngày Dậu")
         elif x==12:
            mbox.showinfo(kq, "Ngày Ngọ")
         else:
            mbox.showerror("Lỗi",e)            
      window = Toplevel() 
      window.title("Chọn ngày tốt trong hôn nhân"); window.geometry('500x100+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Ngày tốt"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Ngày xấu"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Tháng âm lịch: "); lbl1.grid(column=0, row=0)
      lbl2 = Label(tab2, text="Tháng âm lịch: "); lbl2.grid(column=0, row=0)
      lbl3 = Label(tab2, text="(hay gọi là ngày Tu La đoạt giá)"); lbl3.grid(column=3, row=0)
      spin1 = Spinbox(tab1, fg="blue", font=12, from_=1, to=12, width=14); spin1.grid(column=1,row=0)
      spin2 = Spinbox(tab2, fg="blue", font=12, from_=1, to=12, width=14); spin2.grid(column=1,row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn1.grid(column=2, row=0)
      btn2 = Button(tab2, text="Xác nhận", command=clicked2); btn2.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def honNhan8(self):
      def info():
         mbox.showwarning(ct, "Tính chất (tháng):\n- Đại lợi: tốt cho con gái xuất giá\n- Phòng Phu chủ: kỵ với chồng\n- Phòng Thê chủ: kỵ với bản thân\
\n- Phòng Công cô: kỵ với cha mẹ chồng\n- Phòng Nữ phụ mẫu: kỵ với cha mẹ ruột\n(nếu trai gái mồ côi thì không sợ tháng kỵ phòng Công cô, phòng Nữ phụ mẫu)\
\n- Tiểu lợi: kỵ với bà Mai (còn gọi là phòng Mai nhân), nếu không có bà Mai hay chỉ mượn làm giúp lễ cho đủ thì không ngại gì")
      def help():
         mbox.showwarning(hd, "Chọn tuổi con giáp của bạn cho phù hợp tại thanh trắng rồi sau đó nhấn nút Xác nhận")
      def clicked():
         dl="- Đại lợi: "; tl="- Tiểu lợi: "; pcc="- Phòng Công cô: "; ppm="- Phòng Nữ phụ mẫu: "; ppc="- Phòng Phu chủ: "; ptc="- Phòng Thê chủ: "
         t1="1, 7\n"; t2="2, 8\n"; t3="3, 9\n"; t4="4, 10\n"; t5="5, 11\n"; t6="6, 12\n"; x=value.current()
         if x==0 or x==6:
            mbox.showinfo(kq, dl+t6+tl+t1+pcc+t2+ppm+t3+ppc+t4+ptc+t5)
         elif x==1 or x==7:
            mbox.showinfo(kq, dl+t5+tl+t4+pcc+t3+ppm+t2+ppc+t4+ptc+t6)
         elif x==2 or x==8:
            mbox.showinfo(kq, dl+t2+tl+t3+pcc+t4+ppm+t5+ppc+t6+ptc+t1)
         elif x==3 or x==9:
            mbox.showinfo(kq, dl+t1+tl+t6+pcc+t5+ppm+t4+ppc+t3+ptc+t2)
         elif x==4 or x==10:
            mbox.showinfo(kq, dl+t4+tl+t5+pcc+t6+ppm+t1+ppc+t2+ptc+t3)
         elif x==5 or x==11:
            mbox.showinfo(kq, dl+t3+tl+t2+pcc+t1+ppm+t6+ppc+t5+ptc+t4)
         else:
            mbox.showerror("Lỗi",e)
      mbox.showwarning(ly, "Mục này chỉ dành cho bên nhà gái")
      window = Toplevel() 
      window.title("Chọn tháng tốt trong hôn nhân"); window.geometry('500x100+100+200')
      lbl = Label(window, text="Tuổi âm lịch của nữ: "); lbl.grid(column=0, row=0)
      value = Combobox(window); value['values']=chi; value.grid(column=1, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=ct, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()  
   def honNhan9(self):
      def info():
         mbox.showwarning(kn, "Ngũ hành hợp hôn là kết quả của hai mệnh ngũ hành khi phối hợp với nhau")
      def help():
         mbox.showwarning(hd, hdnhhn)
      def clicked():
         x = value1.current(); y = value2.current()
         if x==y==0:
            mbox.showinfo(kq, "Ăn ở với nhau sinh đẻ bất lợi, hay cãi nhau, có khi phải lìa xa. Trừ khi trúng vào quẻ \"Lưỡng Kim\", \"Kim Khuyết\" hoặc\
 \"Lưỡng Kim thành khí")
         elif x==0 and y==1:
            mbox.showinfo(kq, "Hai mạng khắc nhau, khắc xuất, nghèo khổ gian nan, chồng nam vợ bắc")
         elif x==0 and y==2:
            mbox.showinfo(kq, "Thiên duyên tác hợp, con cháu đầy đàn, vợ chồng hoà thuận")
         elif x==0 and y==3:
            mbox.showinfo(kq, "Thường cãi nhau, sinh con khó nuôi, nhà cửa túng nghèo")
         elif x==0 and y==4:
            mbox.showinfo(kq, "Vợ chồng hoà thuận, con cháu đầy đàn, gia đình vui vẻ, lục súc bình an")
         elif x==y==1:
            mbox.showinfo(kq, "Quan lộc tốt, con cháu đông đủ, gia đình hoà hợp")
         elif x==1 and y==0:
            mbox.showinfo(kq, "Hai mạng khắc nhau, trước hợp sau lìa, con cháu bất lợi")                                                   
         elif x==1 and y==2:
            mbox.showinfo(kq, "Tương sinh, tiền tài phú túc, con cháu đông, vợ chồng bách niên giai lão")                                                     
         elif x==1 and y==3:
            mbox.showinfo(kq, "Tự nhiên sinh, tiền tài quan lộc được thịnh vượng, con cháu đông đủ")                                                  
         elif x==1 and y==4:
            mbox.showinfo(kq, "Tương sinh, con cháu đông làm nên đại phú")
         elif x==y==2:
            mbox.showinfo(kq, "Tuy không tốt nhưng điền trạch khá yên, ăn ở với nhau được")                                                   
         elif x==2 and y==0:
            mbox.showinfo(kq, "Sinh tài, sung sướng đến già, con cháu được tốt")
         elif x==2 and y==1:
            mbox.showinfo(kq, "Nhân duyên, vợ chồng ăn ở được bách niên giai lão")
         elif x==2 and y==3:
            mbox.showinfo(kq, "Duyên tự nhiên thành, tuy xấu nhưng được hoà hợp")
         elif x==2 and y==4:
            mbox.showinfo(kq, "Hai mạng khắc nhau, vui vẻ bất thường, làm việc gì cũng khó")                                                    
         elif x==y==3:
            mbox.showinfo(kq, "Giúp nhau có khi thịnh vượng, con cháu đầy đàn")                                                   
         elif x==3 and y==0:
            mbox.showinfo(kq, "Hai mạng khắc nhau, hay cãi vã, kiện cáo, gia đình không yên")
         elif x==3 and y==1:
            mbox.showinfo(kq, "Hợp duyên, gia thất bình an, phúc lộc kiêm toàn")
         elif x==3 and y==2:
            mbox.showinfo(kq, "Tương khắc, vợ chồng chẳng bền duyên, con cháu bất lợi, nhiều gian nguy")
         elif x==3 and y==4:
            mbox.showinfo(kq, "Hữu duyên, tài lộc sung túc, con thảo cháu hiền")
         elif x==y==4:
            mbox.showinfo(kq, "Lưỡng Thổ tương sinh, trước khó sau dễ, lắm của nhiều con")                                                  
         elif x==4 and y==0:
            mbox.showinfo(kq, "Vợ chồng hoà hợp, con cháu thông minh, tài lộc sung túc")
         elif x==4 and y==1:
            mbox.showinfo(kq, "Vợ chồng phải phân ly mỗi người một ngả")                                                  
         elif x==4 and y==2:
            mbox.showinfo(kq, "Tương khắc, trước hợp sau lìa, sinh kế bất lợi")                                                               
         elif x==4 and y==3:                                                     
            mbox.showinfo(kq, "Đắc vị, quan vị dồi dào, con cháu đông đủ giàu sang")
         else:
            mbox.showerror("Lỗi", e)
      window = Toplevel() 
      window.title("Ngũ hành trong hôn nhân"); window.geometry('70050+100+200')
      lbl = Label(window, text="Cung bát quái của nam: "); lbl.grid(column=0, row=0); lbl = Label(window, text="Cung bát quái của nữ:"); lbl.grid(column=2, row=0)
      value1 = Combobox(window); value1['values']=nh; value1.grid(column=1, row=0); value2 = Combobox(window); value2['values']=nh; value2.grid(column=3, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=4, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def honNhan10(self):
      def info():
         mbox.showwarning(kn, hdnd)
      def note():
         mbox.showwarning(ly, "Xem hôn nhân theo Ngũ đế, người nam phải luôn đứng trước rồi mới kết hợp với người nữ. Nếu xem ngược lại sẽ không đúng.")
      def help():
         mbox.showwarning(hd, "Chọn dòng Ngũ đế của hai bạn tại hai thanh trắng rồi nhấn nút Xác nhận (nếu hai bạn chưa biết mình thuộc dòng Ngũ đế nào, vui lòng \
chọn Menu chính > Ngũ đế > Tra ngũ đế)")
      def clicked():
         x = value1.current(); y = value2.current()
         if x==y==0:
            mbox.showinfo(kq, "Rất xấu: ăn ở không được bền lâu, sau có thể chia ly mỗi người mỗi ngả")
         elif x==0 and y==1:
            mbox.showinfo(kq, "Tốt: rất khá giả, làm ăn thịnh phát, lắm của nhiều con")
         elif x==0 and y==2:
            mbox.showinfo(kq, "Tốt: trước phải nghèo khó, từ 30 tuổi trở đi sẽ được khá")
         elif x==0 and y==3:
            mbox.showinfo(kq, "Rất tốt: được thuận thảo và hạnh phúc")
         elif x==0 and y==4:
            mbox.showinfo(kq, "Rất tốt: hoàn toàn hạnh phúc, giàu sang")
         elif x==1 and y==0:
            mbox.showinfo(kq, "Rất xấu: ăn ở xung khắc, sau cùng phải phân ly hai ngả")
         elif x==y==1:
            mbox.showinfo(kq, "Tốt: làm ăn thì đủ dùng tuy không dư dả nhưng bền lâu")
         elif x==1 and y==2:
            mbox.showinfo(kq, "Tốt: sống đến đầu bạc răng long, nếu sinh con trai đầu lòng thì sẽ giàu to")
         elif x==1 and y==3:
            mbox.showinfo(kq, "Rất tốt: trước làm ăn trung bình, từ 30 tuổi trở đi thì được vinh hoa phú quý")
         elif x==1 and y==4:
            mbox.showinfo(kq, "Rất xấu: khắc nhau về mệnh, hay tranh cãi")
         elif x==2 and y==0:
            mbox.showinfo(kq, "Xấu: chồng vợ trước sau cũng chẳng khá, nhưng đặng bền lâu")
         elif x==2 and y==1:
            mbox.showinfo(kq, "Rất tốt: trước cũng như sau, sống được giai lão, giàu sang phú quý")
         elif x==y==2:
            mbox.showinfo(kq, "Rất xấu: xung khắc, gặp tai hoạ luôn luôn rồi sau cũng phân ly")
         elif x==2 and y==3:
            mbox.showinfo(kq, "Rất xấu: rất xung khắc và gặp nhiều tai hoạ")
         elif x==2 and y==4:
            mbox.showinfo(kq, "Tốt: nếu sinh con trai đầu lòng sẽ được giàu sang, làm ăn thịnh vượng")
         elif x==3 and y==0:
            mbox.showinfo(kq, "Rất tốt: trước cũng như sau, đều đặn hoàn toàn hạnh phúc và giàu sang")
         elif x==3 and y==1:
            mbox.showinfo(kq, "Tốt: trước nghèo khổ, sau được giàu sang")
         elif x==3 and y==2:
            mbox.showinfo(kq, "Xấu: vợ chồng bất hoà, luôn luôn tranh cãi")
         elif x==y==3:
            mbox.showinfo(kq, "Tốt: trước nghèo khổ, sau phú quý và đông con")
         elif x==3 and y==4:
            mbox.showinfo(kq, "Rất xấu: vợ chồng bất hoà, khó được bền lâu rồi phải phân ly")
         elif x==4 and y==0:
            mbox.showinfo(kq, "Rất tốt: thuận hoà và giàu sang phú quý")
         elif x==4 and y==1:
            mbox.showinfo(kq, "Tốt: trước phải nghèo khó, từ 30 tuổi trở đi sẽ được khá")
         elif x==4 and y==2:
            mbox.showinfo(kq, "Tốt: sinh con trai đầu lòng sẽ làm ăn phát đạt")
         elif x==4 and y==3:
            mbox.showinfo(kq, "Rất xấu: rất xung khắc và kỵ nuôi con vì khó nuôi sống đến lớn")
         elif x==y==4:
            mbox.showinfo(kq, "Rất tốt: được hạnh phúc, bền duyên và phú quý")
         else:
            mbox.showerror("Lỗi",e)
      window = Toplevel() 
      window.title("Ngũ đế trong hôn nhân"); window.geometry('700x50+100+200')
      lbl = Label(window, text="Dòng ngũ đế của nam: "); lbl.grid(column=0, row=0); lbl = Label(window, text="Dòng ngũ đế của nữ: "); lbl.grid(column=2, row=0)
      value1 = Combobox(window); value1['values']=ngude; value1.grid(column=1, row=0); value2 = Combobox(window); value2['values']=ngude; value2.grid(column=3, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=4, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=kn, command=info); menuBar.add_command(label=ly, command=note); menuBar.add_command(label=hd, command=help)       
      window.mainloop() 
   def nguHanh1(self):
      def info():
         mbox.showwarning(kn, "Người xưa quan niệm trong trời đất (vũ trụ) có năm chất căn bản: Kim (vàng, các kim loại), Mộc (gỗ, cây cối), Thuỷ (nước, hơi nước,\
chất lỏng), Hoả (lửa, hơi nóng, ánh sáng), Thổ (đất, đá, các khoáng vật trừ kim loại) và gọi là Ngũ hành")
      def help():
         mbox.showwarning(hd, hddl1+"\n"+hdal1)
      def clicked1():
         r=int(spin.get())%60
         if r==0 or r==1:
            mbox.showinfo(kq,"Mạng: Thạch Lựu Mộc (cây thạch lựu)\nkhắc: Bích Thượng Thổ (đất trên tường)")
         elif r==2 or r==3:
            mbox.showinfo(kq,"Mạng: Đại Hải Thuỷ (nước biển lớn)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif r==4 or r==5:
            mbox.showinfo(kq,"Mạng: Hải Trung Kim (vàng giữa biển)\nkhắc Bình Địa Mộc (cây sát đất)")
         elif r==6 or r==7:
            mbox.showinfo(kq,"Mạng: Lư Trung Hoả (lửa trong lò)\nkhắc: Kiếm Phong Kim (mũi kiếm vàng)")
         elif r==8 or r==9:
            mbox.showinfo(kq,"Mạng: Đại Lâm Mộc (cây rừng lớn)\nkhắc: Đại Trạch Thổ (đất nhà lớn)")       
         elif r==10 or r==11:
            mbox.showinfo(kq,"Mạng: Lộ Bàn Thổ (đất đường đi)\nkhắc: Tuyền Trung Thuỷ (nước trong suối)")
         elif r==12 or r==13:
            mbox.showinfo(kq,"Mạng: Kiếm Phong Kim (mũi kiếm vàng)\nkhắc: Phúc Đăng Hoả (lửa che đèn)")
         elif r==14 or r==15:
            mbox.showinfo(kq,"Mạng: Sơn Đầu Hoả (lửa đầu núi)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif r==16 or r==17:
            mbox.showinfo(kq,"Mạng: Giang Hạ Thuỷ (nước dưới sông)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif r==18 or r==19:
            mbox.showinfo(kq,"Mạng: Thành Đầu Thổ (đất trên thành)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif r==20 or r==21:
            mbox.showinfo(kq,"Mạng: Bạch Lạp Kim (vàng nến trắng)\nkhắc: Phúc Đăng Hoả (lửa che đèn)")
         elif r==22 or r==23:
            mbox.showinfo(kq,"Mạng: Dương Liễu Mộc (cây dương liễu)\nkhắc: Lộ Bàn Thổ (đất đường đi)")
         elif r==24 or r==25:
            mbox.showinfo(kq,"Mạng: Tuyền Trung Thuỷ (nước trong suối)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif r==26 or r==27:
            mbox.showinfo(kq,"Thổ: Ốc Thượng Thổ (đất trên nhà)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif r==28 or r==29:
            mbox.showinfo(kq,"Mạng: Tích Lịch Hoả (lửa sấm sét)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif r==30 or r==31:
            mbox.showinfo(kq,"Mạng: Tùng Bá Mộc (cây tùng bách)\nkhắc: Lộ Bàn Thổ (đất đường đi)")
         elif r==32 or r==33:
            mbox.showinfo(kq,"Mạng: Trường Lưu Thuỷ (nước chảy dài)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif r==34 or r==35:
            mbox.showinfo(kq,"Mạng: Sa Trung Kim (vàng trong cát)\nkhắc: Thạch Lựu Mộc (cây thạch lựu)")
         elif r==36 or r==37:
            mbox.showinfo(kq,"Mạng: Sơn Hạ Hoả (lửa dưới núi)\nkhắc: Tích Lịch Hoả (lửa sấm sét)")
         elif r==38 or r==39:
            mbox.showinfo(kq,"Mạng: Bình Địa Mộc (cây sát đất)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif r==40 or r==41:
            mbox.showinfo(kq,"Mạng: Bích Thượng Thổ (đất trên tường)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif r==42 or r==43:
            mbox.showinfo(kq,"Mạng: Kim Bạch Kim (vàng trắng vàng)\nkhắc: Lư Trung Hoả (lửa trong lò)")
         elif r==44 or r==45:
            mbox.showinfo(kq,"Mạng: Phúc Đăng Hoả (lửa che đèn)\nkhắc: Thoa Xuyến Kim (vàng trang sức)")
         elif r==46 or r==47:
            mbox.showinfo(kq,"Mạng: Thiên Hà Thuỷ (nước sông trời)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif r==48 or r==49:
            mbox.showinfo(kq,"Mạng: Đại Trạch Thổ (đất nhà lớn)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif r==50 or r==51:
            mbox.showinfo(kq,"Mạng: Thoa Xuyến Kim (vàng trang sức)\nkhắc: Đại Lâm Mộc (cây rừng lớn)")
         elif r==52 or r==53:
            mbox.showinfo(kq,"Mạng: Tang Đố Mộc (cây dâu tằm)\nkhắc: Thành Đầu Thổ (đất trên thành)")
         elif r==54 or r==55:
            mbox.showinfo(kq,"Mạng: Đại Khê Thuỷ (nước suối lớn)\nkhắc: Sơn Hạ Hoả (lửa dưới núi)")
         elif r==56 or r==57:
            mbox.showinfo(kq,"Mạng: Thiên Thượng Hoả (lửa trên trời)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif r==58 or r==59:
            mbox.showinfo(kq,"Mạng: Sa Trung Thổ (đất trong cát)\nkhắc: Dương Liễu Mộc (cây dương liễu)")
         else:
            mbox.showerror("Lỗi",e)
      def clicked2():
         x=value.current()
         if x==0 or x==5:
            mbox.showinfo(kq, "Mạng: Hải Trung Kim (vàng giữa biển)\nkhắc Bình Địa Mộc (cây sát đất)")
         elif x==10 or x==15:
            mbox.showinfo(kq, "Mạng: Lư Trung Hoả (lửa trong lò)\nkhắc: Kiếm Phong Kim (mũi kiếm vàng)")
         elif x==20 or x==25:
            mbox.showinfo(kq, "Mạng: Đại Lâm Mộc (cây rừng lớn)\nkhắc: Đại Trạch Thổ (đất nhà lớn)")       
         elif x==30 or x==35:
            mbox.showinfo(kq, "Mạng: Lộ Bàn Thổ (đất đường đi)\nkhắc: Tuyền Trung Thuỷ (nước trong suối)")
         elif x==40 or x==45:
            mbox.showinfo(kq, "Mạng: Kiếm Phong Kim (mũi kiếm vàng)\nkhắc: Phúc Đăng Hoả (lửa che đèn)")
         elif x==50 or x==55:
            mbox.showinfo(kq, "Mạng: Sơn Đầu Hoả (lửa đầu núi)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif x==1 or x==6:
            mbox.showinfo(kq, "Mạng: Giang Hạ Thuỷ (nước dưới sông)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif x==11 or x==16:
            mbox.showinfo(kq, "Mạng: Thành Đầu Thổ (đất trên thành)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif x==21 or x==26:
            mbox.showinfo(kq, "Mạng: Bạch Lạp Kim (vàng nến trắng)\nkhắc: Phúc Đăng Hoả (lửa che đèn)")
         elif x==31 or x==36:
            mbox.showinfo(kq, "Mạng: Dương Liễu Mộc (cây dương liễu)\nkhắc: Lộ Bàn Thổ (đất đường đi)")
         elif x==41 or x==46:
            mbox.showinfo(kq, "Mạng: Tuyền Trung Thuỷ (nước trong suối)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif x==51 or x==56:
            mbox.showinfo(kq, "Mạng: Ốc Thượng Thổ (đất trên nhà)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif x==2 or x==7:
            mbox.showinfo(kq, "Mạng: Tích Lịch Hoả (lửa sấm sét)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif x==12 or x==17:
            mbox.showinfo(kq, "Mạng: Tùng Bá Mộc (cây tùng bách)\nkhắc: Lộ Bàn Thổ (đất đường đi)")
         elif x==22 or x==27:
            mbox.showinfo(kq, "Mạng: Trường Lưu Thuỷ (nước chảy dài)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif x==32 or x==37:
            mbox.showinfo(kq, "Mạng: Sa Trung Kim (vàng trong cát)\nkhắc: Thạch Lựu Mộc (cây thạch lựu)")
         elif x==42 or x==47:
            mbox.showinfo(kq, "Mạng: Sơn Hạ Hoả (lửa dưới núi)\nkhắc: Tích Lịch Hoả (lửa sấm sét)")
         elif x==52 or x==57:
            mbox.showinfo(kq, "Mạng: Bình Địa Mộc (cây sát đất)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif x==3 or x==8:
            mbox.showinfo(kq, "Mạng: Bích Thượng Thổ (đất trên tường)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif x==13 or x==18:
            mbox.showinfo(kq, "Mạng: Kim Bạch Kim (vàng trắng vàng)\nkhắc: Lư Trung Hoả (lửa trong lò)")
         elif x==23 or x==28:
            mbox.showinfo(kq, "Mạng: Phúc Đăng Hoả (lửa che đèn)\nkhắc: Thoa Xuyến Kim (vàng trang sức)")
         elif x==33 or x==38:
            mbox.showinfo(kq, "Mạng: Thiên Hà Thuỷ (nước sông trời)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif x==43 or x==48:
            mbox.showinfo(kq, "Mạng: Đại Trạch Thổ (đất nhà lớn)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif x==53 or x==58:
            mbox.showinfo(kq, "Mạng: Thoa Xuyến Kim (vàng trang sức)\nkhắc: Đại Lâm Mộc (cây rừng lớn)")
         elif x==4 or x==9:
            mbox.showinfo(kq, "Mạng: Tang Đố Mộc (cây dâu tằm)\nkhắc: Thành Đầu Thổ (đất trên thành)")
         elif x==14 or x==19:
            mbox.showinfo(kq, "Mạng: Đại Khê Thuỷ (nước suối lớn)\nkhắc: Sơn Hạ Hoả (lửa dưới núi)")
         elif x==24 or x==29:
            mbox.showinfo(kq, "Mạng: Thiên Thượng Hoả (lửa trên trời)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif x==34 or x==39:
            mbox.showinfo(kq, "Mạng: Sa Trung Thổ (đất trong cát)\nkhắc: Dương Liễu Mộc (cây dương liễu)")
         elif x==43 or x==49:
            mbox.showinfo(kq, "Mạng: Thạch Lựu Mộc (cây thạch lựu)\nkhắc: Bích Thượng Thổ (đất trên tường)")
         elif x==54 or x==59:
            mbox.showinfo(kq, "Mạng: Đại Hải Thuỷ (nước biển lớn)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Tra ngũ hành"); window.geometry('500x100+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Tra bằng năm sinh dương lịch"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Tra bằng năm sinh âm lịch"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Năm sinh dương lịch: "); lbl2 = Label(tab2, text="Năm sinh âm lịch:")
      lbl1.grid(column=0, row=0); lbl2.grid(column=0, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=9999, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=canchi; value.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn2 = Button(tab2, text="Xác nhận", command=clicked2) 
      btn1.grid(column=2, row=0); btn2.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def nguHanh2(self):
      def info():
         mbox.showwarning(gt, "- Tương sinh, tương khắc:\n+ Người xưa quan niệm trong trời đất (vũ trụ) có năm chất căn bản: Kim (vàng, các kim loại), Mộc (gỗ, cây \
cối), Thuỷ (nước, hơi nước, chất lỏng), Hoả (lửa, hơi nóng, ánh sáng), Thổ (đất, đá, các khoáng vật trừ kim loại) và gọi là Ngũ hành. Trời là dương, đất là âm; theo \
đó cứ hai hành kế tiếp thì hợp gọi là tương sinh, còn đứng cách nhau một hành thì gọi là tương khắc.\n+ Hiện tượng khắc không tồn tại đơn độc; trong tương khắc đã có \
ngụ ý tương sinh, do đó vạn vật tồn tại và phát triển.\n- Ngũ hành tị hoà không hại: Ngũ hành là bản thể của âm dương, nó cũng là sự tồn tại của các dạng vật chất.\
\n- Luật chế hoá:\n+ Chế hoá là ức chế và sinh hoá phối hợp với nhau. Trong chế hoá bao gồm hiện tượng tương sinh và tương khắc. Hai hiện tượng này gắn liền với nhau.\n\
+ Luật chế hoá là một khâu trọng yếu trong thuyết ngũ hành. Khắc và sinh đều cần thiết cho sự giữ gìn cân bằng trong thiên nhiên.")
      def help():
         mbox.showwarning(hd, hdnh)
      def clicked():
         a = value.current()
         if a==0:
            mbox.showinfo(kq, "- Tương sinh: Thổ sinh Kim, Kim sinh Thuỷ\n- Tương khắc: Hoả khắc Kim, Kim khắc Mộc\n- Ngũ hành tị hoà không hại: Kim kiến Kim\n- Quy \
luật chế hoá: Kim khắc Mộc, Mộc sinh Hoả, Hoả khắc Kim")
         elif a==1:
            mbox.showinfo(kq, "- Tương sinh: Thuỷ sinh Mộc, Mộc sinh Hoả\n- Tương khắc: Kim khắc Mộc, Mộc khắc Thổ\n- Ngũ hành tị hoà không hại: Mộc kiến Mộc\n- Quy \
luật chế hoá: Mộc khắc Thổ, Thổ sinh Kim, Kim khắc Mộc")
         elif a==2:
            mbox.showinfo(kq, "- Tương sinh: Kim sinh Thuỷ, Thuỷ sinh Mộc\n- Tương khắc: Thổ khắc Thuỷ, Thuỷ khắc Hoả\n- Ngũ hành tị hoà không hại: Thuỷ kiến Thuỷ\n-\
 Quy luật chế hoá: Thuỷ khắc Hoả, Hoả sinh Thổ, Thổ khắc Thuỷ")
         elif a==3:
            mbox.showinfo(kq, "- Tương sinh: Mộc sinh Hoả, Hoả sinh Thổ\n- Tương khắc: Thuỷ khắc Hoả, Hoả khắc Kim\n- Ngũ hành tị hoà không hại: Hoả kiến Hoả\n- Quy \
luật chế hoá: Hoả khắc Kim, Kim sinh Thuỷ, Thuỷ khắc Hoả")
         elif a==4:
            mbox.showinfo(kq, "- Tương sinh: Hoả sinh Thổ, Thổ sinh Kim\n- Tương khắc: Mộc khắc Thổ, Thổ khắc Thuỷ\n- Ngũ hành tị hoà không hại: Thổ kiến Thổ\n- Quy \
luật chế hoá: Mộc khắc Thổ, Thổ sinh Kim, Kim khắc Mộc")
         else:
            mbox.showerror("Lỗi",e)
      window = Toplevel() 
      window.title("Sơ đồ ngũ hành"); window.geometry('500x100+100+200')
      lbl = Label(window, text="Mệnh ngũ hành: "); lbl.grid(column=0, row=0)
      value = Combobox(window); value['values']=nh; value.grid(column=1, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def nguHanh3(self):
      mbox.showinfo(kq, "*Nguyên tắc 1:\
      \n- Kim do Thổ sinh ra, Thổ nhiều thì Kim bị chôn lấp.\
      \n- Mộc do Thủy sinh, Thủy nhiều thì Mộc bị trôi nổi phiêu bồng.\
      \n- Thổ do Hỏa sinh ra, Hỏa nhiều thì Thổ bị cháy tiêu.\
      \n- Thuỷ do Kim sinh ra, Kim nhiều thì nước bị đục.\
      \n- Hỏa do Mộc sinh sinh ra, Mộc nhiều thì Hỏa càng sáng tỏ.\
      \n* Nguyên tắc 2: Tương sinh\
      \n- Kim sinh Thủy, Thuỷ nhiều thì Kim bị chìm mất.\
      \n- Thuỷ sinh Mộc, Mộc nhiều thì Thủy bị cạn (thu rút lại).\
      \n- Mộc sinh Hỏa, Hỏa nhiều thì Mộc bị cháy hết.\
      \n- Hỏa sinh Thổ, Thổ nhiều thì Hỏa tối lại.\
      \n- Thổ sinh Kim, Kim nhiều thì Thổ yếu (mất nhiều năng lực).\
      \n\n*Nguyên tắc 3:\
      \n- Kim suy (ít) gặp Hỏa, tất bị đun, chảy ra.\
      \n- Hỏa yếu gặp Thủy, tất bị tắt, tiêu diệt.\
      \n- Thủy yếu (ít) gặp Thổ, tất bị ứ tắc.\
      \n- Thổ suy (ít) gặp Mộc, tất gặp sự đảo lộn bế hãm (mất tính chất nguyên thủy).\
      \n- Mộc yếu gặp Kim, tất bị chém gãy.\
      \n\n*Nguyên tắc 4:\
      \n- Kim mạnh (nhiều) được Thủy, sự nhọn sắc mòn gãy bớt dần đi.\
      \n- Thuỷ mạnh (nhiều) được Mộc, thế sức mạnh bị tiết bớt đi.\
      \n- Mộc mạnh (nhiều) được Hỏa, sự cứng rắn bị hóa giải bớt dần đi.\
      \n- Hỏa mạnh (nhiều) được Thổ, sự sáng rực bị giữ bớt lại.\
      \n- Thổ mạnh (nhiều) được Kim, sự ủng hộ (giúp sức) bị chế bớt lại.\
      \n\n*Nguyên tắc 5: Tương khắc\
      \n- Kim khắc Mộc, nhưng Mộc rắn thì Kim gãy, sứt mẻ.\
      \n- Mộc khắc Thổ, nhưng Thổ nhiều, nặng thì Mộc gãy.\
      \n- Thổ khắc Thủy, nhưng Thủy nhiều thì Thổ bị trôi đi.\
      \n- Thủy khắc Hỏa, nhưng Hỏa bốc cháy lớn, thì Thủy bị cạn bốc hơi đi.\
      \n- Hỏa khắc Kim, nhưng Kim nhiều chảy tràn ra thì Hỏa tắt.")
   def nguHanh4(self):
      def info():
         mbox.showwarning(gt, "Bảng tương ứng ngũ hành cho ta biết các yếu tố: mùa, phương hướng, thời tiết-khí, màu sắc, mùi vị... của các mệnh Ngũ hành.")
      def help():
         mbox.showwarning(hd, hdnh)
      def clicked():
         a = value.current()
         if a==0:
            mbox.showinfo(kq, "- Bốn mùa: Thu\n- Bốn phương: Tây\n- Thời tiết, khí: Mát\n- Màu sắc: Trắng\n- Mùi vị: Cay\n- Bát quái: Càn, Đoài\n- Thiên can: Canh, \
Tân\n- Địa chi: Thân, Dậu")
         elif a==1:
            mbox.showinfo(kq, "- Bốn mùa: Xuân\n- Bốn phương: Đông\n- Thời tiết, khí: Ấm\n- Màu sắc: Xanh\n- Mùi vị: Chua\n- Bát quái: Tốn, Chấn\n- Thiên can: Giáp, \
Ất\n- Địa chi: Dần, Mão")
         elif a==2:
            mbox.showinfo(kq, "- Bốn mùa: Đông\n- Bốn phương: Bắc\n- Thời tiết, khí: Lạnh\n- Màu sắc: Đen\n- Mùi vị: Mặn\n- Bát quái: Khảm\n- Thiên can: Nhâm, Quý\
\n- Địa chi: Hợi, Tý")
         elif a==3:
            mbox.showinfo(kq, "- Bốn mùa: Hạ\n- Bốn phương: Nam\n- Thời tiết, khí: Nóng\n- Màu sắc: Đỏ\n- Mùi vị: Đắng\n- Bát quái: Ly\n- Thiên can: Bính, Đinh\
\n- Địa chi: Tỵ, Ngọ")
         elif a==4:
            mbox.showinfo(kq, "- Bốn mùa: Cuối các mùa\n- Bốn phương: Giữa các phương (Đông Nam, Tây Nam, Đông Bắc, Tây Bắc)\n- Thời tiết, khí: Ẩm\n- Màu sắc: Vàng\
\n- Mùi vị: Ngọt\n- Bát quái: Cấn, Khôn\n- Thiên can: Mậu, Kỷ\n- Địa chi: Thìn, Tuất, Sửu, Mùi")
         else:
            mbox.showerror("Lỗi",e)            
      window = Toplevel() 
      window.title("Bảng tương ứng ngũ hành"); window.geometry('500x100+100+200')
      lbl = Label(window, text="Mệnh ngũ hành: "); lbl.grid(column=0, row=0)
      value = Combobox(window); value['values']=nh; value.grid(column=1, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def batQuai1(self):
      def info():
         mbox.showwarning(kn, "Có trên có dưới, có tả có hữu, có trước có sau nên gọi là Vũ. Có xưa có nay, có quá khứ có tương lai nên gọi là Trụ. \
Trong Vũ trụ có ánh sáng, tối tăm, ngày đêm, mưa gió, sấm chớp, sông hồ, ao rạch... nên luận thành Bát quái gồm có: "+str(bq)+"\n*Lưu ý: \
đây là cung Bát quái (cung Ký sinh), loại cung về vận mệnh đặc điểm của từng người, vận hạn cứ theo đó mà định hình. \
Còn loại cung còn lại (cung Bát trạch) chỉ là cung liên quan đến điền thổ, đến chỗ ở, việc xây cất nhà cửa, có sự phân biệt giữa nam và nữ, không nên nhầm lẫn.") 
      def help():
         mbox.showwarning(hd, hdbq)
      def clicked1():
         r=int(spin.get())%60
         if r==1 or r==7 or r==14 or r==23 or r==28 or r==40 or r==46:
            mbox.showinfo(kq,"Cung: Càn\n- Hướng: Tây Bắc\n- Tượng trưng: Trời, mặt trời, ban ngày, ánh sáng, cha, phái nam\n- Thuộc: dương Kim")
         elif r==6 or r==11 or r==18 or r==32 or r==35 or r==44 or r==50 or r==56:
            mbox.showinfo(kq,"Cung: Khảm\n- Hướng: chính Bắc\n- Tượng trưng: nước, con trai thứ\n- Thuộc: dương Thuỷ")
         elif r==3 or r==9 or r==16 or r==27 or r==30 or r==39 or r==42 or r==48 or r==54:
            mbox.showinfo(kq,"Cung: Cấn\n- Hướng: Đông Bắc\n- Tượng trưng: núi non, con trai út\n- Thuộc: dương Thổ")
         elif r==4 or r==13 or r==20 or r==25 or r==37 or r==52 or r==58:
            mbox.showinfo(kq,"Cung: Chấn\n- Hướng: chính Đông\n- Tượng trưng: sấm sét, con trai trưởng\n- Thuộc: dương Mộc")
         elif r==5 or r==21 or r==26 or r==38 or r==53 or r==59:
            mbox.showinfo(kq,"Cung: Tốn\n- Hướng: Đông Nam\n- Tượng trưng: gió băo, con gái trưởng\n- Thuộc: âm Mộc")
         elif r==10 or r==17 or r==22 or r==31 or r==34 or r==43 or r==49 or r==55:
            mbox.showinfo(kq,"Cung: Ly\n- Hướng: chính Nam\n- Tượng trưng: lửa, con gái thứ\n- Thuộc: âm Hoả")
         elif r==0 or r==12 or r==19 or r==24 or r==33 or r==36 or r==51 or r==57:
            mbox.showinfo(kq,"Cung: Khôn\n- Hướng: Tây Nam\n- Tượng trưng: Đất, mặt trăng, ban đêm, bóng tối, mẹ, phái nữ\n- Thuộc: âm Thổ")
         elif r==2 or r==8 or r==15 or r==29 or r==41 or r==45 or r==47:
            mbox.showinfo(kq,"Cung: Đoài\n- Hướng: chính Tây\n- Tượng trưng: ao hồ, sông rạch, con gái út\n- Thuộc: âm Kim")
         else:
            mbox.showerror("Lỗi",e)
      def clicked2():
         x=value.current()
         if x==2 or x==3 or x==15 or x==33 or x==36 or x==49 or x==50:
            mbox.showinfo(kq,"Cung: Càn\n- Hướng: Tây Bắc\n- Tượng trưng: Trời, mặt trời, ban ngày, ánh sáng, cha, phái nam\n- Thuộc: dương Kim")
         elif x==10 or x==22 or x==23 or x==24 or x==37 or x==53:
            mbox.showinfo(kq,"Cung: Khảm\n- Hướng: chính Bắc\n- Tượng trưng: nước, con trai thứ\n- Thuộc: dương Thuỷ")
         elif x==1 or x==12 or x==13 or x==14 or x==25 or x==44 or x==56 or x==57 or x==59:
            mbox.showinfo(kq,"Cung: Cấn\n- Hướng: Đông Bắc\n- Tượng trưng: núi non, con trai út\n- Thuộc: dương Thổ")
         elif x==0 or x==4 or x==5 or x==21 or x==34 or x==39 or x==45 or x==46 or x==47:
            mbox.showinfo(kq,"Cung: Chấn\n- Hướng: chính Đông\n- Tượng trưng: sấm sét, con trai trưởng\n- Thuộc: dương Mộc")
         elif x==5 or x==9 or x==26 or x==35 or x==51 or x==52:
            mbox.showinfo(kq,"Cung: Tốn\n- Hướng: Đông Nam\n- Tượng trưng: gió băo, con gái trưởng\n- Thuộc: âm Mộc")
         elif x==6 or x==17 or x==18 or x==30 or x==31 or x==48:
            mbox.showinfo(kq,"Cung: Ly\n- Hướng: chính Nam\n- Tượng trưng: lửa, con gái thứ\n- Thuộc: âm Hoả")
         elif x==11 or x==16 or x==19 or x==27 or x==29 or x==40 or x==41 or x==42 or x==43 or x==58:
            mbox.showinfo(kq,"Cung: Khôn\n- Hướng: Tây Nam\n- Tượng trưng: Đất, mặt trăng, ban đêm, bóng tối, mẹ, phái nữ\n- Thuộc: âm Thổ")
         elif x==7 or x==8 or x==20 or x==28 or x==38 or x==54 or x==55:
            mbox.showinfo(kq,"Cung: Đoài\n- Hướng: chính Tây\n- Tượng trưng: ao hồ, sông rạch, con gái út\n- Thuộc: âm Kim")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Tra bát quái"); window.geometry('500x100+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Tra bằng năm sinh dương lịch"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Tra bằng năm sinh âm lịch"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Năm sinh dương lịch: "); lbl2 = Label(tab2, text="Năm sinh âm lịch:")
      lbl1.grid(column=0, row=0); lbl2.grid(column=0, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=9999, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=canchi; value.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn2 = Button(tab2, text="Xác nhận", command=clicked2) 
      btn1.grid(column=2, row=0); btn2.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop() 
   def thienCan(self):
      def info():
         mbox.showwarning(kn, "Có tất cả 10 thiên can: "+str(can))
      def help():
         mbox.showwarning(hd, hdtc)
      def clicked():
         if thiencan.current()==0:
            mbox.showinfo(kq,"- Thuộc tính: Dương\n- Ngũ hành: Mộc\n- Hợp: Kỷ\n- Phá: Mậu\n- Xung: Canh")
         elif thiencan.current()==1:            
            mbox.showinfo(kq,'- Thuộc tính: Âm\n- Ngũ hành: Mộc\n- Hợp: Canh\n- Phá: Kỷ\n- Xung: Tân')
         elif thiencan.current()==2:            
            mbox.showinfo(kq,'- Thuộc tính: Dương\n- Ngũ hành: Hoả\n- Hợp: Tân\n- Phá: Canh\n- Xung: Nhâm')
         elif thiencan.current()==3:            
            mbox.showinfo(kq,'- Thuộc tính: Âm\n- Ngũ hành: Hoả\n- Hợp: Nhâm\n- Phá: Tân\n- Xung: Quý')
         elif thiencan.current()==4:            
            mbox.showinfo(kq,'- Thuộc tính: Dương\n- Ngũ hành: Thổ\n- Hợp: Quý\n- Phá: Nhâm\n- Xung: Giáp')
         elif thiencan.current()==5:            
            mbox.showinfo(kq,'- Thuộc tính: Âm\n- Ngũ hành: Thổ\n- Hợp: Giáp\n- Phá: Quý\n- Xung: Ất')
         elif thiencan.current()==6:            
            mbox.showinfo(kq,'- Thuộc tính: Dương\n- Ngũ hành: Kim\n- Hợp: Ất\n- Phá: Giáp\n- Xung: Bính')
         elif thiencan.current()==7:            
            mbox.showinfo(kq,'- Thuộc tính: Âm\n- Ngũ hành: Kim\n- Hợp: Bính\n- Phá: Ất\n- Xung: Đinh')
         elif thiencan.current()==8:            
            mbox.showinfo(kq,'- Thuộc tính: Dương\n- Ngũ hành: Thuỷ\n- Hợp: Đinh\n- Phá: Bính\n- Xung: Mậu')
         elif thiencan.current()==9:            
            mbox.showinfo(kq,'- Thuộc tính: Âm\n- Ngũ hành: Thuỷ\n- Hợp: Mậu\n- Phá: Đinh\n- Xung: Kỷ')
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Thiên can"); window.geometry('400x50+200+200')
      lbl = Label(window, text="Thiên can của bạn:"); lbl.grid(column=0, row=0)      
      thiencan = Combobox(window); thiencan['values']=can; thiencan.grid(column=1, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop() 
   def diaChi1(self):
      def info():
         mbox.showwarning(kn, "- Có tất cả 12 địa chi (con giáp): "+str(chi)+"\n- 12 địa chi (con giáp) tương hợp có ba loại: nhị hợp, tam hợp và lục xung")
      def help():
         mbox.showwarning(hd, hddc)
      def clicked():
         if diachi.current()==0:
            mbox.showinfo(kq,'* Thuộc tính: Dương\n* Ngũ hành: Thuỷ\n* Nhị hợp: Tý - Sửu\n* Tam hợp: Thân - Tý - Thìn\n* Lục xung: Tý - Ngọ')
         elif diachi.current()==1:
            mbox.showinfo(kq,'* Thuộc tính: Âm\n* Ngũ hành: Thổ\n* Nhị hợp: Tý - Sửu\n* Tam hợp: Tỵ - Dậu - Sửu\n* Lục xung: Mùi - Sửu')
         elif diachi.current()==2:
            mbox.showinfo(kq,'* Thuộc tính: Dương\n* Ngũ hành: Mộc\n* Nhị hợp: Dần - Hợi\n* Tam hợp: Dần - Ngọ - Tuất\n* Lục xung: Thân - Dần')
         elif diachi.current()==3:
            mbox.showinfo(kq,'* Thuộc tính: Âm\n* Ngũ hành: Mộc\n* Nhị hợp: Măo/Mẹo - Tuất\n* Tam hợp: Hợi - Măo/Mẹo - Mùi\n* Lục xung: Măo/Mẹo - Dậu')
         elif diachi.current()==4:
            mbox.showinfo(kq,'* Thuộc tính: Dương\n* Ngũ hành: Thổ\n* Nhị hợp: Thìn - Dậu\n* Tam hợp: Thân - Tý - Thìn\n* Lục xung: Thìn - Tuất')
         elif diachi.current()==5:
            mbox.showinfo(kq,'* Thuộc tính: Âm\n* Ngũ hành: Hoả\n* Nhị hợp: Tỵ - Thân\n* Tam hợp: Tỵ - Dậu - Sửu\n* Lục xung: Hợi - Tỵ')
         elif diachi.current()==6:
            mbox.showinfo(kq,'* Thuộc tính: Dương\n* Ngũ hành: Hoả\n* Nhị hợp: Ngọ - Mùi\n* Tam hợp: Dần - Ngọ - Tuất\n* Lục xung: Tý - Ngọ')
         elif diachi.current()==7:
            mbox.showinfo(kq,'* Thuộc tính: Âm\n* Ngũ hành: Thổ\n* Nhị hợp: Ngọ - Mùi\n* Tam hợp: Hợi - Măo/Mẹo - Mùi\n* Lục xung: Mùi - Sửu')
         elif diachi.current()==8:
            mbox.showinfo(kq,'* Thuộc tính: Dương\n* Ngũ hành: Kim\n* Nhị hợp: Tỵ - Thân\n* Tam hợp: Thân - Tý - Thìn\n* Lục xung: Thân - Dần')
         elif diachi.current()==9:
            mbox.showinfo(kq,'* Thuộc tính: Âm\n* Ngũ hành: Kim\n* Nhị hợp: Thìn - Dậu\n* Tam hợp: Tỵ - Dậu - Sửu\n* Lục xung: Măo/Mẹo - Dậu')
         elif diachi.current()==10:
            mbox.showinfo(kq,'* Thuộc tính: Dương\n* Ngũ hành: Thổ\n* Nhị hợp: Măo/Mẹo - Tuất\n* Tam hợp: Dần - Ngọ - Tuất\n* Lục xung: Thìn - Tuất')
         elif diachi.current()==11:
            mbox.showinfo(kq,'* Thuộc tính: Âm\n* Ngũ hành: Thuỷ\n* Nhị hợp: Dần - Hợi\n* Tam hợp: Hợi - Măo/Mẹo - Mùi\n* Lục xung: Hợi - Tỵ')
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Địa chi (con giáp)"); window.geometry('500x50+200+200')
      lbl=Label(window, text="Địa chi (con giáp) của bạn: "); lbl.grid(column=0, row=0)      
      diachi=Combobox(window); diachi['values']=chi; diachi.grid(column=1, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def diaChi2(self):
      def info():
         mbox.showwarning(kn, "Mối tương quan giữa 12 con giáp cả về phương diện cá nhân lẫn sự nghiệp là một bộ phận quan trọng trong việc tiên đoán số mạng. \
Chúng ta có thể tham khảo kết quả sau đây để biết thêm về sự tương quan dó. Nó bao gồm luôn cả những ảnh hưởng của thời khắc được sinh ra cũng như những khía cạnh \
đặc biệt khác thường thuộc số mạng. Nhờ vào đó bạn sẽ thấy được sự hoà hợp hay xung khắc giữa các con giáp với nhau")
      def help():
         mbox.showwarning(hd, hddchn)
      def clicked():
         x=diachi1.current(); y=diachi2.current()
         if x<0 or x>11 or y<0 or y>11:
            mbox.showerror("Lỗi",e)
         elif (x==0 and y==4) or (x==0 and  y==8) or (x==1 and y==5) or (x==1 and y==9) or (x==2 and y==6) or (x==2 and y==10) or (x==3 and y==7)\
            or (x==3 and y==11) or (x==4 and y==0) or (x==4 and y==8) or (x==5 and y==1) or (x==5 and y==9) or (x==6 and y==2) or (x==6 and y==10)\
            or (x==7 and y==3) or (x==7 and y==11) or (x==8 and y==4) or (x==8 and y==0) or (x==9 and y==5) or (x==9 and y==1) or (x==10 and y==6)\
            or (x==10 and y==2) or (x==11 and y==3) or (x==11 and y==7):
            mbox.showinfo(kq, "Con giáp của hai bạn rất hợp nhau!")
         elif (x==0 and y==1) or (x==0 and y==5) or (x==1 and y==0) or (x==1 and y==3) or (x==2 and y==9) or (x==2 and y==11) or (x==3 and y==4)\
              or (x==3 and y==10) or (x==4 and y==3) or (x==4 and y==11) or (x==5 and y==4) or (x==5 and y==7) or (x==6 and y==4) or (x==6 and y==7)\
              or (x==7 and y==2) or (x==7 and y==6) or (x==y==8) or (x==8 and y==11) or (x==9 and y==4) or (x==9 and y==7) or (x==10 and y==3)\
              or (x==y==10) or (x==11 and y==0) or (x==11 and y==2):
            mbox.showinfo(kq, "Con giáp của hai bạn hợp nhau!")
         elif (x==y==0) or (x==0 and y==2) or (x==0 and y==10) or (x==0 and y==11) or (x==y==1) or (x==1 and y==4) or (x==1 and y==8) or (x==1 and y==11)\
              or (x==y==2) or (x==2 and y==1) or (x==2 and y==4) or (x==2 and y==7) or (x==y==3) or (x==3 and y==0) or (x==3 and y==1) or (x==3 and y==5)\
              or (x==4 and y==2) or (x==4 and y==5) or (x==4 and y==7) or (x==4 and y==9) or (x==y==5) or (x==5 and y==0) or (x==5 and y==3) or (x==5 and y==10)\
              or (x==6 and y==5) or (x==6 and y==8) or (x==6 and y==9) or (x==6 and y==11) or (x==y==7) or (x==7 and y==4) or (x==7 and y==5) or (x==7 and y==8)\
              or (x==8 and y==1) or (x==8 and y==7) or (x==8 and y==9) or (x==8 and y==10) or (x==9 and y==2) or (x==9 and y==6) or (x==9 and y==10)\
              or (x==9 and y==11) or (x==10 and y==0) or (x==10 and y==5) or (x==10 and y==8) or (x==10 and y==11) or (x==11 and y==1) or (x==11 and y==4)\
              or (x==11 and y==9) or (x==11 and y==10):
            mbox.showinfo(kq, "Con giáp của hai bạn có thể làm việc chung!")
         else:
            mbox.showinfo(kq, "Con giáp của hai bạn khắc nhau!")
      window = Toplevel() 
      window.title("Sự tương quan giữa 12 con giáp"); window.geometry('700x50+100+200')
      lbl1 = Label(window, text="Con giáp của bạn: "); lbl1.grid(column=0, row=0)
      lbl2 = Label(window, text="Con giáp của đối tác:"); lbl2.grid(column=2, row=0)       
      diachi1 = Combobox(window); diachi1['values'] = chi; diachi1.grid(column=1, row=0)
      diachi2 = Combobox(window); diachi2['values'] = chi; diachi2.grid(column=3, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=4, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def duongLich1(self):
      def help():
         mbox.showwarning(hd, hddl2)
      def clicked1():
         global d, m, y
         d=int(spin1.get()); m=int(spin2.get()); y=int(spin3.get())
         if (d==31 and m==4) or (d==31 and m==6) or (d==31 and m==9) or (d==31 and m==11) or (d==31 and m==2) or (d==30 and m==2) or (d==29 and m==2 and y%4!=0)\
            or d<1 or d>31 or m<1 or m>12 or y<1:
            mbox.showerror("Lỗi",e)
         else:
            clicked()
      def clicked2():
         today = date.today()
         global d, m, y
         d = int(today.strftime("%d")); m = int(today.strftime("%m")); y = int(today.strftime("%y"))
         clicked()
      def clicked():
         if y%4==0:
            a=29
         else:
            a=28
         if m==1:
            b=d
         elif m==2:
            b=31+d
         elif m==3:
            b=31+a+d
         elif m==4:
            b=31+a+31+d
         elif m==5:
            b=31+a+31+30+d
         elif m==6:
            b=31+a+31+30+31+d
         elif m==7:
            b=31+a+31+30+31+30+d
         elif m==8:
            b=31+a+31+30+31+30+31+d
         elif m==9:
            b=31+a+31+30+31+30+31+31+d
         elif m==10:
            b=31+a+31+30+31+30+31+31+30+d
         elif m==11:
            b=31+a+31+30+31+30+31+31+30+31+d
         elif m==12:
            b=31+a+31+30+31+30+31+31+30+31+30+d
         w=math.ceil(b/7)
         mbox.showinfo(kq, "Ngày thứ %d và tuần thứ %d trong năm" %(b, w+1))
      window = Toplevel() 
      window.title("Tra thứ tự ngày, tuần trong năm"); window.geometry('800x50+100+200')
      lbl1 = Label(window, text="Ngày: "); lbl2 = Label(window, text="Tháng: "); lbl3 = Label(window, text="Năm: ")
      lbl1.grid(column=0, row=0); lbl2.grid(column=2, row=0); lbl3.grid(column=4, row=0)
      spin1 = Spinbox(window, fg="blue", font=12, from_=1, to=31, width=14); spin1.grid(column=1,row=0)
      spin2 = Spinbox(window, fg="blue", font=12, from_=1, to=12, width=14); spin2.grid(column=3,row=0)
      spin3 = Spinbox(window, fg="blue", font=12, from_=1, to=9999, width=14); spin3.grid(column=5,row=0) 
      btn1 = Button(window, text="Xác nhận", command=clicked1); btn1.grid(column=6, row=0)
      btn2 = Button(window, text="Xem ngày hôm nay", command=clicked2); btn2.grid(column=7, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def duongLich2(self):
      def help():
         mbox.showwarning(hd, hddl2)
      def clicked1():
         global d, m, y
         d=int(spin1.get()); m=int(spin2.get()); y=int(spin3.get())
         if (d==31 and m==4) or (d==31 and m==6) or (d==31 and m==9) or (d==31 and m==11) or (d==31 and m==2) or (d==30 and m==2) or (d==29 and m==2 and y%4!=0)\
            or d<1 or d>31 or m<1 or m>12 or y<1:
            mbox.showerror("Lỗi",e)
         else:
            clicked()
      def clicked2():
         today = date.today()
         global d, m, y
         d = int(today.strftime("%d")); m = int(today.strftime("%m")); y = int(today.strftime("%y"))
         clicked()
      def clicked():
         t=(d+((153*(m+12*((14-m)/12)-3)+2)/5)+(365*(y+4800-((14-m)/12)))+((y+4800-((14-m)/12))/4)-((y+4800-((14-m)/12))/100)+((y+4800-((14-m)/12))/400)-32045)%7
         t=math.floor(t)
         if t==0:
            mbox.showinfo(kq, "Ngày thứ 7 trong tuần")
         elif t==1:
            mbox.showinfo(kq, "Ngày Chủ nhật trong tuần")
         else:
            mbox.showinfo(kq, "Ngày thứ %d trong tuần" %(t))      
      window = Toplevel() 
      window.title("Tra thứ trong tuần"); window.geometry('800x50+100+200')
      lbl1 = Label(window, text="Ngày: "); lbl2 = Label(window, text="Tháng: "); lbl3 = Label(window, text="Năm: ")
      lbl1.grid(column=0, row=0); lbl2.grid(column=2, row=0); lbl3.grid(column=4, row=0)
      spin1 = Spinbox(window, fg="blue", font=12, from_=1, to=31, width=14); spin1.grid(column=1,row=0)
      spin2 = Spinbox(window, fg="blue", font=12, from_=1, to=12, width=14); spin2.grid(column=3,row=0)
      spin3 = Spinbox(window, fg="blue", font=12, from_=1, to=9999, width=14); spin3.grid(column=5,row=0)
      btn1 = Button(window, text="Xác nhận", command=clicked1); btn1.grid(column=6, row=0)
      btn2 = Button(window, text="Xem ngày hôm nay", command=clicked2); btn2.grid(column=7, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop() 
   def amLich1(self):
      def info():
         mbox.showwarning(gt, "- Nước Trung Hoa cổ làm lịch từ đời Phục Hy, bắt đầu từ năm Giáp Tý rồi luân chuyển đi cho đến ngày nay. Từ năm 1984 đến năm 2043 là \
chu kỳ 78 kể từ chu kỳ đầu tiên ấy. Từ thời Đông Hán về sau mới dùng can chi để ghi cả năm, ngày, tháng, giờ. Đời Hán Vũ Đế lấy tháng Dần làm tháng đầu năm, tháng hai \
là tháng Mão,... cho đến tháng chạp là tháng Sửu và ghép với 10 can, khởi đầu là Giáp... đến can cuối cùng là Quý rồi lại tiếp tục trở về Giáp...\n- Tên can chi của \
tháng gọi là Nguyệt Kiến, tên can chi của ngày gọi là Nguyệt Sóc.\n- Mỗi ngày đêm có 24 giờ nhưng theo can chi thì chỉ có 12 giờ. Dương lịch được ấn định từ 12 giờ \
khuya hay 0 giờ được kể là giờ bước qua ngày mới thì âm lịch cũng phải bắt đầu từ giờ Tý là qua ngày khác. Đừng nên lầm tưởng rằng giờ Tý bắt đầu từ 11 giờ khuya, \
như vậy sẽ lạc hẳn hệ thống âm dương, làm mất vẻ tôn trọng thiêng liêng của thời khắc giao thừa mỗi năm, lúc âm dương giao thái vạn vật phát sinh.")
      def help():
         mbox.showwarning(hd, "- Đổi năm:\n"+hddl1+"\n- Đổi tháng:\nChọn Thiên can cho phù hợp tại thanh trắng thứ nhất và "+hdal2+"\n- Đổi giờ:\nChọn Thiên can cho \
phù hợp tại thanh trắng thứ nhất và "+hdchi+"\n- Xem giờ:\nNhập giờ bạn muốn xem tại thanh trắng rồi sau đó nhấn nút Xác nhận hoặc Xem giờ hiện tại bằng cách nhấn \
nút Xem giờ hiện tại")
      def clicked1():
         y=int(spin1.get())
         x=y%10; z=y%12
         if y<1:
            mbox.showerror("Lỗi",e)
         else:
            if x==0:
               a=can[6]
            elif x==1:
               a=can[7]
            elif x==2:
               a=can[8]
            elif x==3:
               a=can[9]
            elif x==4:
               a=can[0]
            elif x==5:
               a=can[1]
            elif x==6:
               a=can[2]
            elif x==7:
               a=can[3]
            elif x==8:
               a=can[4]
            else:
               a=can[5]
            if z==0:
               b=chi[8]
            elif z==1:
               b=chi[9]
            elif z==2:
               b=chi[10]
            elif z==3:
               b=chi[11]
            elif z==4:
               b=chi[0]
            elif z==5:
               b=chi[1]
            elif z==6:
               b=chi[2]
            elif z==7:
               b=chi[3]
            elif z==8:
               b=chi[4]
            elif z==9:
               b=chi[5]
            elif z==10:
               b=chi[6]
            else:
               b=chi[7]
            mbox.showinfo(kq, "Năm can chi là: "+a+' '+b)
      def clicked2():
         p = value1.current(); m = int(spin2.get())
         if p<0 or p>9 or m<1 or m>12:
            mbox.showerror("Lỗi",e)
         else:
            if p==0 or p==5:
               if m<8:
                  a=can[m+1]
               else:
                  a=can[m-9]
            elif p==1 or p==6:
               if m<6:
                  a=can[m+3]
               else:
                  a=can[m-7]
            elif p==2 or p==7:
               if m<4:
                  a=can[m+5]
               else:
                  a=can[m-5]
            elif p==3 or p==8:
               if m<2:
                  a=can[m+7]
               else:
                  a=can[m-3]
            elif p==4 or p==9:
               if m<10:
                  a=can[m-1]
               else:
                  a=can[m-11]
            if m<10:
               b = chi[m+1]
            else:
               b = chi[m-11]
            mbox.showinfo(kq, "Nguyệt Kiến (can chi của tháng) là: "+a+' '+b)
      def clicked3():
         p = value2.current(); h = value3.current();
         if p<0 or p>9 or h<0 or h>11:
            mbox.showerror("Lỗi",e)
         else:
            if p==0 or p==5:
               if h<10:
                  a=can[h]
               else:
                  a=can[h-10]
            elif p==1 or p==6:
               if h<9:
                  a=can[h+1]
               else:
                  a=can[h-9]
            elif p==2 or p==7:
               if h<6:
                  a=can[h+4]
               else:
                  a=can[h-6]
            elif p==3 or p==8:
               if h<4:
                  a=can[h+6]
               else:
                  a=can[h-4]
            elif p==4 or p==9:
               if h<2:
                  a=can[h+8]
               else:
                  a=can[h-2]
            b = chi[h]
            mbox.showinfo(kq, "Can chi của giờ là: "+a+' '+b)
      def clicked4():
         a = int(spin3.get())
         if a==0 or a==1:
            mbox.showinfo(kq, "Giờ Tý (canh ba)")
         elif a==2 or a==3:
            mbox.showinfo(kq, "Giờ Sửu (canh tư)")
         elif a==4 or a==5:
            mbox.showinfo(kq, "Giờ Dần (canh năm)")
         elif a==6 or a==7:
            mbox.showinfo(kq, "Giờ Mão")
         elif a==8 or a==9:
            mbox.showinfo(kq, "Giờ Thìn")
         elif a==10 or a==11:
            mbox.showinfo(kq, "Giờ Tỵ")
         elif a==12 or a==13:
            mbox.showinfo(kq, "Giờ Ngọ")
         elif a==14 or a==15:
            mbox.showinfo(kq, "Giờ Mùi")
         elif a==16 or a==17:
            mbox.showinfo(kq, "Giờ Thân")
         elif a==18 or a==19:
            mbox.showinfo(kq, "Giờ Dậu")
         elif a==20 or a==21:
            mbox.showinfo(kq, "Giờ Tuất (canh một)")
         elif a==22 or a==23:
            mbox.showinfo(kq, "Giờ Hợi (canh hai)")
         else:
            mbox.showerror("Lỗi",e)
      def today4():
         today = date.today()
         global a
         a = int(today.strftime("%H"))-1
         clicked4()
      def list4():
         mbox.showinfo(ds, "- Dương khắc (giờ): \n+ Tý: 0-2\n+ Dần: 4-6\n+ Thìn: 8-10\n+ Ngọ: 12-14\n+ Thân: 16-18\n+ Tuất: 20-22\n- Âm khắc (giờ): \n+ Sửu: 2-4\
\n+ Mão: 6-8\n+ Tỵ: 10-12\n+ Mùi: 14-16\n+ Dậu: 18-20\n+ Hợi: 22-0\n- Ban đêm (giờ):\n+ Canh một: 20-22 (8-10 giờ tối)\n+ Canh hai: 22-0 (10-12 giờ khuya)\n+ Canh \
ba: 0-2 (12-2 giờ sáng)\n+ Canh tư: 2-4 (giờ sáng)\n+ Canh năm: 4-6 (giờ sáng)")
      window = Toplevel() 
      window.title("Đổi dương lịch ra âm lịch"); window.geometry('700x100+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control); tab3 = ttk.Frame(tab_control); tab4 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Đổi năm"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Đổi tháng"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab3, text="Đổi giờ"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab4, text="Xem giờ"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Năm dương lịch: "); lbl1.grid(column=0, row=0)
      lbl2 = Label(tab2, text="Can của năm âm lịch: "); lbl2.grid(column=0, row=0)
      lbl21 = Label(tab2, text="Tháng âm lịch: "); lbl21.grid(column=2, row=0)
      lbl3 = Label(tab3, text="Can của ngày âm lịch: "); lbl3.grid(column=0, row=0)
      lbl31 = Label(tab3, text="Giờ: "); lbl31.grid(column=2, row=0)
      lbl4 = Label(tab4, text="Giờ (định dạng 24h): "); lbl4.grid(column=0, row=0)
      spin1 = Spinbox(tab1, fg="blue", font=12, from_=1, to=9999, width=14); spin1.grid(column=1,row=0)
      spin2 = Spinbox(tab2, fg="blue", font=12, from_=1, to=12, width=14); spin2.grid(column=3,row=0)
      spin3 = Spinbox(tab4, fg="blue", font=12, from_=1, to=12, width=14); spin3.grid(column=1,row=0)
      value1 = Combobox(tab2); value1['values']=can; value1.grid(column=1, row=0)
      value2 = Combobox(tab3); value2['values']=can; value2.grid(column=1, row=0)
      value3 = Combobox(tab3); value3['values']=chi; value3.grid(column=3, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn1.grid(column=2, row=0)
      btn2 = Button(tab2, text="Xác nhận", command=clicked2); btn2.grid(column=4, row=0)
      btn3 = Button(tab3, text="Xác nhận", command=clicked3); btn3.grid(column=4, row=0)
      btn4 = Button(tab4, text="Xác nhận", command=clicked4); btn4.grid(column=4, row=0)
      btn41 = Button(tab4, text="Xem giờ hiện tại", command=today4); btn41.grid(column=5, row=0)
      btn42 = Button(tab4, text="Danh sách", command=list4); btn42.grid(column=6, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def amLich2(self):
      def info():
         mbox.showwarning(gt, "Xem ngày âm lịch")
      def help():
         mbox.showwarning(hd, hddl2)
      def clicked():
            START_YEAR = 1901
            month_DAY_BIT = 12
            month_NUM_BIT = 13
            def _cnDay(_day):
               _cn_day=numDay
               return _cn_day[(_day - 1) % 30]

            def _cnMonth(_month):
                """ 阴历-月
                    Arg:
                        type(_day) int 13 数字形式的阴历-月
                    Return:
                        String "闰正月"
                """
                _cn_month = ["giêng", "hai", "ba", "tư", "năm", "sáu", "bảy", "tám", "chín", "mười", "mười một", "chạp"]
                leap = (_month >> 4 ) &0xf
                m = _month &0xf
                _month = _cn_month[(m - 1) % 12]
                if leap == m:
                    _month = "nhuận" + _month
                return _month

            def _cnYear(_year):
                """ 阴历-年
                    Arg:
                        type(_year) int 2018 数字形式的年份
                    Return:
                        String "戊戍[狗]" 汉字形式的年份
                """
                _tian_gan = can
                _di_zhi = chi
                _sheng_xiao = congiap
                return _tian_gan[(_year - 4) % 10] +' '+ _di_zhi[(_year - 4) % 12] +' '+ '[' + _sheng_xiao[(_year - 4) % 12] + ']'
            def _upperYear(_date):
                """ 年份大写 如：二零一八 """
                _upper_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                _upper_year = ""
                for i in str(_date.year):
                    _upper_year += _upper_num[int(i)]
                return _upper_year

            def _upperWeek(_date):
                """ 星期大写 如：星期一 """
                _week_day = thu
                return _week_day[_date.weekday()]


            def _cnMonthDays(_cn_year, _cn_month):
                """ 计算阴历月天数
                    Arg:
                        type(_cn_year) int 2018 数字年份
                        type(_cn_month) int 6 数字阴历月份    
                    Return:
                        int 30或29,该年闰月，闰月天数
                """
                # 农历数据 每个元素的存储格式如下：
                #   16~13    12          11~0
                #  闰几月 闰月日数  1~12月份农历日数
                _cn_month_list = [
                0x00752, 0x00ea5, 0x0ab2a, 0x0064b, 0x00a9b, 0x09aa6, 0x0056a, 0x00b59, 0x04baa, 0x00752, # 1901 ~ 1910
                0x0cda5, 0x00b25, 0x00a4b, 0x0ba4b, 0x002ad, 0x0056b, 0x045b5, 0x00da9, 0x0fe92, 0x00e92, # 1911 ~ 1920
                0x00d25, 0x0ad2d, 0x00a56, 0x002b6, 0x09ad5, 0x006d4, 0x00ea9, 0x04f4a, 0x00e92, 0x0c6a6, # 1921 ~ 1930
                0x0052b, 0x00a57, 0x0b956, 0x00b5a, 0x006d4, 0x07761, 0x00749, 0x0fb13, 0x00a93, 0x0052b, # 1931 ~ 1940
                0x0d51b, 0x00aad, 0x0056a, 0x09da5, 0x00ba4, 0x00b49, 0x04d4b, 0x00a95, 0x0eaad, 0x00536, # 1941 ~ 1950
                0x00aad, 0x0baca, 0x005b2, 0x00da5, 0x07ea2, 0x00d4a, 0x10595, 0x00a97, 0x00556, 0x0c575, # 1951 ~ 1960
                0x00ad5, 0x006d2, 0x08755, 0x00ea5, 0x0064a, 0x0664f, 0x00a9b, 0x0eada, 0x0056a, 0x00b69, # 1961 ~ 1970
                0x0abb2, 0x00b52, 0x00b25, 0x08b2b, 0x00a4b, 0x10aab, 0x002ad, 0x0056d, 0x0d5a9, 0x00da9, # 1971 ~ 1980
                0x00d92, 0x08e95, 0x00d25, 0x14e4d, 0x00a56, 0x002b6, 0x0c2f5, 0x006d5, 0x00ea9, 0x0af52, # 1981 ~ 1990
                0x00e92, 0x00d26, 0x0652e, 0x00a57, 0x10ad6, 0x0035a, 0x006d5, 0x0ab69, 0x00749, 0x00693, # 1991 ~ 2000
                0x08a9b, 0x0052b, 0x00a5b, 0x04aae, 0x0056a, 0x0edd5, 0x00ba4, 0x00b49, 0x0ad53, 0x00a95, # 2001 ~ 2010
                0x0052d, 0x0855d, 0x00ab5, 0x12baa, 0x005d2, 0x00da5, 0x0de8a, 0x00d4a, 0x00c95, 0x08a9e, # 2011 ~ 2020
                0x00556, 0x00ab5, 0x04ada, 0x006d2, 0x0c765, 0x00725, 0x0064b, 0x0a657, 0x00cab, 0x0055a, # 2021 ~ 2030
                0x0656e, 0x00b69, 0x16f52, 0x00b52, 0x00b25, 0x0dd0b, 0x00a4b, 0x004ab, 0x0a2bb, 0x005ad, # 2031 ~ 2040
                0x00b6a, 0x04daa, 0x00d92, 0x0eea5, 0x00d25, 0x00a55, 0x0ba4d, 0x004b6, 0x005b5, 0x076d2, # 2041 ~ 2050
                0x00ec9, 0x10f92, 0x00e92, 0x00d26, 0x0d516, 0x00a57, 0x00556, 0x09365, 0x00755, 0x00749, # 2051 ~ 2060
                0x0674b, 0x00693, 0x0eaab, 0x0052b, 0x00a5b, 0x0aaba, 0x0056a, 0x00b65, 0x08baa, 0x00b4a, # 2061 ~ 2070
                0x10d95, 0x00a95, 0x0052d, 0x0c56d, 0x00ab5, 0x005aa, 0x085d5, 0x00da5, 0x00d4a, 0x06e4d, # 2071 ~ 2080
                0x00c96, 0x0ecce, 0x00556, 0x00ab5, 0x0bad2, 0x006d2, 0x00ea5, 0x0872a, 0x0068b, 0x10697, # 2081 ~ 2090
                0x004ab, 0x0055b, 0x0d556, 0x00b6a, 0x00752, 0x08b95, 0x00b45, 0x00a8b, 0x04a4f, ]        # 2091 ~ 2100
                if (_cn_year < START_YEAR):
                    return 30

                leap_month, leap_day, month_day = 0, 0, 0 # 闰几月，该月多少天 传入月份多少天

                tmp = _cn_month_list[_cn_year - START_YEAR]

                if tmp & ( 1 << (_cn_month -1)):
                    month_day = 30
                else:
                    month_day = 29

                # 闰月
                leap_month = (tmp >> month_NUM_BIT) & 0xf
                if leap_month:
                    if (tmp & ( 1<<month_DAY_BIT)):
                        leap_day = 30
                    else:
                        leap_day = 29

                return [month_day, leap_month, leap_day]

            def _getNumCnDate(_date):
                """ 获取数字形式的农历日期
                    Args:
                        _date = datetime(year, month, day)
                    Return:
                        _year, _month, _day
                        返回的月份，高4bit为闰月月份，低4bit为其它正常月份
                """
                # 农历数据 每个元素的存储格式如下：
                #7~6    5~1
                #春节月  春节日
                _cn_year_list = [
                0x53, 0x48, 0x3d, 0x50, 0x44, 0x39, 0x4d, 0x42, 0x36, 0x4a, # 1901 ~ 1910
                0x3e, 0x52, 0x46, 0x3a, 0x4e, 0x43, 0x37, 0x4b, 0x41, 0x54, # 1911 ~ 1920
                0x48, 0x3c, 0x50, 0x45, 0x38, 0x4d, 0x42, 0x37, 0x4a, 0x3e, # 1921 ~ 1930
                0x51, 0x46, 0x3a, 0x4e, 0x44, 0x38, 0x4b, 0x3f, 0x53, 0x48, # 1931 ~ 1940
                0x3b, 0x4f, 0x45, 0x39, 0x4d, 0x42, 0x36, 0x4a, 0x3d, 0x51, # 1941 ~ 1950
                0x46, 0x3b, 0x4e, 0x43, 0x38, 0x4c, 0x3f, 0x52, 0x48, 0x3c, # 1951 ~ 1960
                0x4f, 0x45, 0x39, 0x4d, 0x42, 0x35, 0x49, 0x3e, 0x51, 0x46, # 1961 ~ 1970
                0x3b, 0x4f, 0x43, 0x37, 0x4b, 0x3f, 0x52, 0x47, 0x3c, 0x50, # 1971 ~ 1980
                0x45, 0x39, 0x4d, 0x42, 0x54, 0x49, 0x3d, 0x51, 0x46, 0x3b, # 1981 ~ 1990
                0x4f, 0x44, 0x37, 0x4a, 0x3f, 0x53, 0x47, 0x3c, 0x50, 0x45, # 1991 ~ 2000
                0x38, 0x4c, 0x41, 0x36, 0x49, 0x3d, 0x52, 0x47, 0x3a, 0x4e, # 2001 ~ 2010
                0x43, 0x37, 0x4a, 0x3f, 0x53, 0x48, 0x3c, 0x50, 0x45, 0x39, # 2011 ~ 2020
                0x4c, 0x41, 0x36, 0x4a, 0x3d, 0x51, 0x46, 0x3a, 0x4d, 0x43, # 2021 ~ 2030
                0x37, 0x4b, 0x3f, 0x53, 0x48, 0x3c, 0x4f, 0x44, 0x38, 0x4c, # 2031 ~ 2040
                0x41, 0x36, 0x4a, 0x3e, 0x51, 0x46, 0x3a, 0x4e, 0x42, 0x37, # 2041 ~ 2050
                0x4b, 0x41, 0x53, 0x48, 0x3c, 0x4f, 0x44, 0x38, 0x4c, 0x42, # 2051 ~ 2060
                0x35, 0x49, 0x3d, 0x51, 0x45, 0x3a, 0x4e, 0x43, 0x37, 0x4b, # 2061 ~ 2070
                0x3f, 0x53, 0x47, 0x3b, 0x4f, 0x45, 0x38, 0x4c, 0x42, 0x36, # 2071 ~ 2080
                0x49, 0x3d, 0x51, 0x46, 0x3a, 0x4e, 0x43, 0x38, 0x4a, 0x3e, # 2081 ~ 2090
                0x52, 0x47, 0x3b, 0x4f, 0x45, 0x39, 0x4c, 0x41, 0x35, 0x49, # 2091 ~ 2100
                ]
                _year, _month, _day = _date.year, 1, 1
                _code_year = _cn_year_list[_year - START_YEAR]
                """ 获取当前日期与当年春节的差日 """
                _span_days = (_date - datetime(_year, ((_code_year >> 5) & 0x3), ((_code_year >> 0) & 0x1f))).days
                #print("span_day: ", _span_days)
                
                if (_span_days >= 0):
                    """ 新年后推算日期，差日依序减月份天数，直到不足一个月，剪的次数为月数，剩余部分为日数 """
                    """ 先获取闰月 """
                    _month_days,_leap_month, _leap_day = _cnMonthDays(_year, _month)
                    while _span_days >= _month_days:
                        """ 获取当前月份天数，从差日中扣除 """
                        _span_days -= _month_days
                        if (_month == _leap_month):
                            """ 如果当月还是闰月 """
                            _month_days = _leap_day
                            if (_span_days < _month_days):
                                """ 指定日期在闰月中 ???"""
                                _month = (leap_month<<4) | month
                                break
                            """ 否则扣除闰月天数，月份加一 """
                            _span_days -= _month_days
                        _month += 1 
                        _month_days = _cnMonthDays(_year, _month)[0]
                    _day += _span_days
                    return _year, _month, _day
                else:
                    """ 新年前倒推去年日期 """
                    _month = 12
                    _year -= 1
                    _month_days,_leap_month, _leap_day = _cnMonthDays(_year, _month)
                    while abs(_span_days) > _month_days:
                        _span_days += _month_days
                        _month -= 1
                        if (_month == _leap_month):
                            _month_days = _leap_day
                            if (abs(_span_days) <= _month_days): # 指定日期在闰月中
                                _month = (leap_month<<4) | month
                                break
                            _span_days += _month_days
                        _month_days = _cnMonthDays(_year, _month)[0]
                    _day += (_month_days + _span_days) # 从月份总数中倒扣 得到天数
                    return _year, _month, _day
                    
            def getCnDate(_date):
                """ 获取完整的农历日期
                    Args:
                        _date = datetime(year, month, day)
                    Return:
                        "农历 xx[x]年 xxxx年x月xx 星期x"
                """
                (_year, _month, _day) = _getNumCnDate(_date)
                return "- Năm: %s \n- Tháng: %s \n- Ngày: %s" % (_cnYear(_year), _cnMonth(_month), _cnDay(_day))

            def getCnYear(_date):
                """ 获取农历年份
                    Args:
                        _date = datetime(year, month, day)
                    Return:
                        "x月"
                """
                _year = _getNumCnDate(_date)[0]
                return "%s年" %_cnYear(_year)

            def getCnMonth(_date):    
                """ 获取农历月份
                    Args:
                        _date = datetime(year, month, day)
                    Return:
                        "xx"
                """
                _month = _getNumCnDate(_date)[1]
                return "%s" %_cnMonth(_month)

            def getCnDay(_date):
                """ 获取农历日
                    Args:
                        _date = datetime(year, month, day)
                    Return:
                        "农历 xx[x]年 xxxx年x月xx 星期x"
                """
                _day = _getNumCnDate(_date)[2]
                return "%s" %_cnDay(_day)
            def getSolarTerms(_date):
                """ 查询节气 待改查表法
                    输入日期
                    输出节气 "\0" "立春" 
                """
                #当前流程：
                #判断世纪
                #获取年份后两位
                #根据月份选择公式
                #矫正
                #对应日期
                #查表法流程:
                #检索当年节气表
                #检索当月节气日
                #判断是否相等
                _jie_qi = [
                ["\0"],
                ["小寒", "大寒"],  # 1月
                ["立春", "雨水"],  # 2月
                ["惊蛰", "春分"],  # 3月
                ["清明", "谷雨"],  # 4月
                ["立夏", "小满"],  # 5月
                ["芒种", "夏至"],  # 6月
                ["小暑", "大暑"],  # 7月
                ["立秋", "处暑"],  # 8月
                ["白露", "秋分"],  # 9月
                ["寒露", "霜降"],  # 10月
                ["立冬", "小雪"],  # 11月
                ["大雪", "冬至"]]  # 12月s
                _century = 0
                if _date.year >= 2000:
                    _century = 1 
                _year = _date.year%100
                _month =_date.month
                _D = 0.2422
                _M = 1
                if _date.month == 1:
                    #小寒
                    _C = [ 6.11, 5.4055 ][_century]
                    _solar_day = (_year * _D + _C) - ((_year-1)/4)
                    if _date.year == 1982:#矫正
                        _solar_day += 1
                    if _date.year == 2019:#矫正
                        _solar_day -= 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    _C = [ 20.84, 20.12][_century]
                    _solar_day = (_year * _D + _C) - ((_year-1)/4)
                    if _date.year == 2082:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 2:
                    #立春
                    _C = [ 4.15, 3.87 ][_century]
                    _solar_day = (_year * _D + _C) - ((_year-1)/4)
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #雨水
                    _C = [ 18.73, 18.73 ][_century]
                    _solar_day = (_year * _D + _C) - ((_year-1)/4)
                    if _date.year == 2026:#矫正
                        _solar_day -= 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 3:
                    #惊蛰
                    _C = [ 5.63, 5.63][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #春分
                    _C = [ 20.646, 20.646][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 2084:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 4:
                    #清明
                    _C = [ 5.59, 4.81 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #谷雨
                    _C = [ 20.888, 20.1][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 5:
                    #立夏
                    _C = [ 6.318, 5.52 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1911:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #小满
                    _C = [ 21.86, 21.04 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 2008:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 6:
                    #芒种
                    _C = [ 6.5, 5.678 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1902:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #夏至
                    _C = [ 22.20, 21.37 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1928:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 7:
                    #小暑
                    _C = [ 7.928, 7.108 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1925|_date.year == 2016:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #大暑
                    _C = [ 23.65, 22.83 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1922:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 8:
                    #立秋
                    _C = [ 8.35, 7.5 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 2002:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #处暑
                    _C = [ 23.95, 23.13 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 9:
                    #白露
                    _C = [ 8.44, 7.646 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1927:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #秋分
                    _C = [ 23.822, 23.042 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1942:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 10:
                    #寒露
                    _C = [ 9.098, 8.318 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #霜降
                    _C = [ 24.218, 23.438 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 2089:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 11:
                    #立冬
                    _C = [ 8.218, 7.438 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 2089:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #小雪
                    _C = [ 23.08, 22.36 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1978:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                _M += 1
                if _date.month == 12:
                    #大雪
                    _C = [ 7.9, 7.18 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1954:#矫正
                        _solar_day += 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][0]
                    #冬至
                    _C = [ 22.60, 21.94 ][_century]
                    _solar_day = (_year * _D + _C) - (_year/4)
                    if _date.year == 1918|_date.year == 2021:#矫正
                        _solar_day -= 1
                    if _date.day == _solar_day//1:
                        return _jie_qi[_M][1]
                return _jie_qi[0][0]
            def _showMonth(_date):
               mbox.showinfo(kq, getCnDate(_date))
            pre = x
            _showMonth(x)#测试所有入口
            late = x
            pop= late-pre
      def clicked1():
         d = int(spin1.get()); m = int(spin2.get()); y = int(spin3.get())
         if (d==31 and m==4) or (d==31 and m==6) or (d==31 and m==9) or (d==31 and m==11) or (d==31 and m==2) or (d==30 and m==2) or (d==29 and m==2 and y%4!=0)\
            or d<1 or d>31 or m<1 or m>12 or y<1901 or y>2099:
            mbox.showwarning("Lỗi",e+"\n(yêu cầu năm chỉ từ 1901-2100)")
         else:
            global i, t, x
            i = date(y, m, d+1); t = time(1, 1)
            x = datetime.combine(i, t)
            clicked()
            def nguyetKien():
               p = y%10; global a
               if p==0 or p==5:
                  if m<10:
                     a=can[m+3]
                  else:
                     a=can[m-7]
               elif p==1 or p==6:
                  a=can[m+3]
               elif p==2 or p==7:
                  a=can[m+5]
               elif p==3 or p==8:
                  a=can[m+7]
               elif p==4 or p==9:
                  if m<8:
                     a=can[m+1]
                  else:
                     a=can[m-9]
               print(a)
            nguyetKien()
      def clicked2():
         global x
         x = datetime.now()
         clicked()
      window = Toplevel()
      window.title("Xem ngày âm lịch"); window.geometry('800x50+100+200')
      lbl1 = Label(window, text="Ngày: "); lbl2 = Label(window, text="Tháng: "); lbl3 = Label(window, text="Năm: ")
      lbl1.grid(column=0, row=0); lbl2.grid(column=2, row=0); lbl3.grid(column=4, row=0)
      spin1 = Spinbox(window, fg="blue", font=12, from_=1, to=31, width=14); spin1.grid(column=1,row=0)
      spin2 = Spinbox(window, fg="blue", font=12, from_=1, to=12, width=14); spin2.grid(column=3,row=0)
      spin3 = Spinbox(window, fg="blue", font=12, from_=1, to=9999, width=14); spin3.grid(column=5,row=0)
      btn = Button(window, text="Xác nhận", command=clicked1); btn.grid(column=6, row=0)
      btn = Button(window, text="Xem ngày hôm nay", command=clicked2); btn.grid(column=7, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def nguDe1(self):
      def info():
         mbox.showwarning(gt, hdnd)
      def help():
         mbox.showwarning(hd, hddl2+" hoặc "+hdal1)
      def clicked1():
         r=int(spin.get())%60
         if r==52 or r==53:
            mbox.showinfo(kq,ngude[0]+": quan lộc, vất vả")
         elif r==8 or r==9 or r==22 or r==30 or r==31:
            mbox.showinfo(kq,ngude[0]+": trường mạng")
         elif r==23 or r==38 or r==39:
            mbox.showinfo(kq,ngude[0]+": hiền từ, phú quý")
         elif r==0 or r==1:
            mbox.showinfo(kq,ngude[0]+": cô bần")
         elif r==18 or r==19 or r==26 or r==27 or r==56 or r==57:
            mbox.showinfo(kq,ngude[1]+": phú quý")
         elif r==40 or r==41:
            mbox.showinfo(kq,ngude[1]+": quan lộc, bần hàn")
         elif r==10 or r==11:
            mbox.showinfo(kq,ngude[1]+": cô bần")
         elif r==48 or r==49:
            mbox.showinfo(kq,ngude[1]+": quan lộc")
         elif r==4 or r==5 or r==12 or r==13 or r==35 or r==42 or r==43 or r==50 or r==51:
            mbox.showinfo(kq,ngude[2]+": phú quý")
         elif r==20 or r==21:
            mbox.showinfo(kq,ngude[2]+": trường mạng")
         elif r==34:
            mbox.showinfo(kq,ngude[2]+": an mạng, phú quý")
         elif r==16 or r==17:
            mbox.showinfo(kq,ngude[3]+": cô bần")
         elif r==24 or r==25 or r==54 or r==55:
            mbox.showinfo(kq,ngude[3]+": phú quý")
         elif r==32 or r==33:
            mbox.showinfo(kq,ngude[3]+": trường mạng")
         elif r==46 or r==47:
            mbox.showinfo(kq,ngude[3]+": vất vả")
         elif r==2 or r==3:
            mbox.showinfo(kq,ngude[3]+": quan lộc")
         elif r==6 or r==7 or r==14 or r==15 or r==36 or r==37 or r==52 or r==58:
            mbox.showinfo(kq,ngude[4]+": cô bần")
         elif r==28 or r==29 or r==59:
            mbox.showinfo(kq,ngude[4]+": phú quý")
         elif r==44 or r==45:
            mbox.showinfo(kq,ngude[4]+": vất vả")
         else:
            mbox.showerror("Lỗi",e)
      def clicked2():
         x=value.current()
         if x==9 or x==14:
            mbox.showinfo(kq,ngude[0]+": quan lộc, vất vả")
         elif x==12 or x==17 or x==31:
            mbox.showinfo(kq,ngude[0]+": trường mạng")
         elif x==36 or x==52 or x==57:
            mbox.showinfo(kq,ngude[0]+": hiền từ, phú quý")
         elif x==43 or x==49:
            mbox.showinfo(kq,ngude[0]+": cô bần")
         elif x==11 or x==16 or x==24 or x==29 or x==51 or x==56:
            mbox.showinfo(kq,ngude[1]+": phú quý")
         elif x==3 or x==8:
            mbox.showinfo(kq,ngude[1]+": quan lộc, bần hàn")
         elif x==30 or x==35:
            mbox.showinfo(kq,ngude[1]+": cô bần")
         elif x==44 or x==48:
            mbox.showinfo(kq,ngude[1]+": quan lộc")
         elif x==0 or x==5 or x==13 or x==18 or x==37 or x==40 or x==45 or x==53:
            mbox.showinfo(kq,ngude[2]+": phú quý")
         elif x==20 or x==21 or x==26:
            mbox.showinfo(kq,ngude[2]+": trường mạng")
         elif x==32:
            mbox.showinfo(kq,ngude[2]+": an mạng, phú quý")
         elif x==1 or x==6:
            mbox.showinfo(kq,ngude[4]+": cô bần")
         elif x==14 or x==19 or x==41 or x==46:
            mbox.showinfo(kq,ngude[4]+": phú quý")
         elif x==22 or x==27:
            mbox.showinfo(kq,ngude[4]+": trường mạng")
         elif x==33 or x==38:
            mbox.showinfo(kq,ngude[4]+": vất vả")
         elif x==54 or x==59:
            mbox.showinfo(kq,ngude[4]+": quan lộc")
         elif x==4 or x==10 or x==15 or x==42 or x==47 or x==50 or x==55:
            mbox.showinfo(kq,ngude[3]+": cô bần")
         elif x==2 or x==7 or x==39:
            mbox.showinfo(kq,ngude[3]+": phú quý")
         elif x==23 or x==28:
            mbox.showinfo(kq,ngude[3]+": vất vả")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Tra Ngũ đế"); window.geometry('500x50+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Tra bằng năm sinh dương lịch"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Tra bằng năm sinh âm lịch"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Năm sinh dương lịch: "); lbl2 = Label(tab2, text="Năm sinh âm lịch:")
      lbl1.grid(column=0, row=0); lbl2.grid(column=0, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=9999, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=canchi; value.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn2 = Button(tab2, text="Xác nhận", command=clicked2) 
      btn1.grid(column=2, row=0); btn2.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def nguDe2(self):
      def info():
         mbox.showwarning(gt, hdnd)
      def help():
         mbox.showwarning(hd, "Chọn dòng Ngũ đế phù hợp với bạn tại thanh trắng rồi nhấn nút Xác nhận (nếu bạn chưa biết mình thuộc dòng Ngũ đế nào, vui lòng chọn \
Menu chính > Ngũ đế > Tra ngũ đế)")
      def clicked():
         if value.current()==0:
            mbox.showinfo(kq, "- Người có tính tình hoà nhã, điềm đạm, giàu tưởng tượng, dung hoà, thích cảnh u nhàn tĩnh mịch, trầm tư mặc tưởng một \
mình. Nhiều cảm hứng trước những tuyệt tác văn chương, thích tranh cổ, yêu mến loài vật, thích xem những loại sách về triết lý, đạo đức..., thích tôn giáo, hay \
cúng bái Tổ tiên. Lòng tự ái cao, liêm chính, ít gặp tai nạn.\n- Yểu điệu, gương mặt tròn, nước da trắng, môi son, bàn tay mềm mại, đi đứng \
chỉnh tề, ăn nói nghiêm trang, mừng giận chẳng lộ ra ngoài mặt. Cặm cụi tỉ mỉ, thích làm việc nội trợ, thêu thùa khéo, ham chưng diện cho con cái, biết trang trí \
trong nhà.\n+ Đàn ông: phần nhiều thích nghề như giáo sư, hoạ sĩ, nhạc sĩ, văn sĩ; đa tình nhưng lại bạc số.\n+ Đàn bà: rất giàu tình cảm, yêu mến gia đình, tính \
hơi nhát, không có chí tranh đấu, an phận thủ thường. Sạch sẽ, khéo léo, chung tình, ghen ngầm, con cái đông.")
         elif value.current()==1:
            mbox.showinfo(kq, "- Tính tình mạnh mẽ, minh mẫn, sáng suốt, can đảm, liều lĩnh, gan dạ phi thường, thường đấu tranh quyết liệt. Ham mê \
lợi danh.\n- Người tướng mạo to lớn, sức vóc mạnh mẽ, ăn to nói lớn, đi đứng lanh lẹ, ham võ nghệ, thích thể thao, săn bắn. Họ ít xúc động, \
trung hậu, khi phẫn nộ cũng lắm ngang tàng. Phần đông họ không được nhã nhặn nhưng thành thực, có mưu lược. Những nghề mà họ thích nhất là lái xe, thầu khoán, kỹ \
nghệ, quân đội.\n- Tính cương quyết, ít chịu lùi bước trước cảnh ngộ khó khăn, quyết làm cho được mới thôi, khi phán đoán thì rất trầm tĩnh. Những ông thẩm phán, \
các vị quan chức thuộc ngành hành chính đều chịu ảnh hưởng của con nhà "+ngude[1]+" cả. Họ rất nghiêm khắc và chẳng dung thứ những kẻ cường bạo, giữ trọn bổn phận \
thiên về lý trí hơn là tình cảm. Người có nước da màu mật ong, hơi ngăm ngăm, đàn ông râu nhiều, đàn bà tóc nhiều, cứng, đen. Chăn nuôi sức vật thì dễ dàng mau \
lớn, không hao. \n+ Đàn bà: tướng mạo mảnh khảnh, tính \
nết đoan trang, ăn nói rõ ràng, siêng năng, cần kiệm, ít bạn bè, ăn uống đạm bạc. Lãnh đạm chồng con, nhưng trong tâm thì lại keo sơn chung thuỷ. Ít để ý đến việc \
người khác, không ưa hát xướng, không thích du ngoạn. Đặc tính của họ là giữ của, vì tiết kiệm mà thành ra có phần mất cảm tình với họ hàng thân thích, bạn bè.")
         elif value.current()==2:
            mbox.showinfo(kq, "- Người có hình tướng nhỏ, đều đặn, cân đối, gương mặt vừa phải, da trắng hồng, môi đỏ tiếng nói thanh tao lảnh lót, hình dáng dễ \
thương.\n- Người có tâm linh, ngoại giao giỏi, lanh lợi, tiên tiến. Người khôn ngoan, đa mưu túc trí, cử chỉ khoan hòa, kiên tâm để đạt mục tiêu, có đủ lý luận và \
quyến rũ bạn bè theo ý kiến của mình. Có khi vì muốn đạt thành nguyện vọng mà làm cả chuyện phi pháp.\n+ Đàn bà con nhà "+ngude[2]+" thì rất lãnh đạm về tình ái, \
thường hay lạm dụng tình cảm của kẻ khác mà làm ra tiền bạc, thích nơi sang giàu quyền quý, lúc nào cũng muốn tạo thành sự nghiệp to lớn, một địa vị trong xã hội.\n\
- Tuy vậy, không được cảm tình của bạn bè và trong gia quyến vì tính cứng cỏi hay khích bác người, ỷ mình có sáng kiến khôn ngoan, lời nói trôi chảy cho nên cũng hay \
làm mất lòng người. Nếu gặp hoàn cảnh thuận tiện thì họ có thể làm những nghề như thương mại, kỹ nghệ, thầu khoán, luật sư, bác sĩ, nhà toán học... Đôi khi có những \
tật xấu như xảo trá, gian hùng hay ăn chơi phóng đãng, vì nhiều mối tình nên họ chẳng chung tình với ai cả. Phần nhiều ấy không phải là tiền định mà chỉ do hoàn \
cảnh tạo nên vì thiếu sự giáo dục của gia đình.")
         elif value.current()==3:
            mbox.showinfo(kq, "- Người có tính tình ngay thẳng, uy nghiêm, giải quyết công việc một cách dứt khoát, trọng kỉ luật, ít nói nhưng không kiêu hãnh. Lạc \
quan và rất tự tin nơi tài chí sẵn có. Tính người trầm tĩnh thận trọng, có lòng tự ái, trường thọ, trong đời ít gặp tai nạn.\n- Người có thân hình hơi mập nước da \
sậm, đôi mắt sáng, nói lớn, thanh tao, đầu cao trán rộng và miệng cũng rộng, răng lớn cằm vuông.\n- Làm giàu chậm nhưng vững bền, gặp cảnh khó khăn đến mấy cũng chịu \
đựng nổi.\n+ Đàn ông con dòng "+ngude[3]+" rất có đạo nghĩa, yêu mến vợ con, chung tình và cũng đòi hỏi khắt khe ở người yêu.\n+ Đàn bà con dòng "+ngude[3]+" là một \
người vợ quý, mẹ hiền, nội trợ giỏi. Sinh đẻ dễ dàng, không hay đau ốm, chuộng thuần phong mỹ tục, tôn trọng trời phật, kính yêu ông bà, cha mẹ và người lớn tuổi. \
Không xa hoa phung phí, tính tiết kiệm thanh cần, không thích trưng diện son phấn, chung tình, ít nói, làm việc nhiều, yêu gia đình tha thiết, không hay giúp đỡ \
người khác nhưng không bao giờ lường lận ai. Dù gặp hoàn cảnh thế nào cũng được hưởng hạnh phúc lúc tuổi già.\n=> Có thể nói là khuôn mẫu cho luân lý, kỷ luật, công \
bình, liêm chính, nhẫn nại, an phận.")                          
         elif value.current()==4:
            mbox.showinfo(kq, "- Người có tính tình khô khan, nguội lạnh. Nghiêm trang tề chỉnh, nhẫn nại mọi việc, đạm bạc đơn giản, chịu khó tích trữ của cải.\n\
- Gian nan cực khổ, có chí kiên gan, chịu đựng cay đắng giỏi, nhờ vậy mà thành công trong mọi công việc, như nhà thong thái, bác học, triết học, các tu sĩ của các \
tôn giáo, rất thích những sách xưa đồ cổ. Những vị lương y đại tài, những nhà tu hành khổ hạnh đều chịu ảnh hưởng của dòng này.\n- Nước da đen nhánh, tay chân thô \
kệch, ít nói. Tướng cao, răng dài, tóc cứng gọn gàng, chẳng có mỹ thuật lắm nhưng được siêng năng, tằn tiện, giàu lòng hy sinh cho gia đình, dạy dỗ con cái đúng lễ. \
\n+ Đàn bà: thích nơi thanh lịch, hay cúng quải thờ phụng ông bà, trời phật.\n+ Đàn ông: ở hoàn cảnh bình thường thì phần đông hay rượu chè, làm việc nặng nhọc, xã \
giao kém, ít nói, cộc cằn, có khi đến mức thô bỉ, chẳng hay để ý đến việc của người khác. Họ có thể trở nên hung ác, nếu gặp sự bức ép, lại cũng vì quá thành thật \
mà hay bị người ta lừa gạt.")
         else:
            mbox.showerror("Lỗi",e)
      window = Toplevel()
      window.title("Tính cách và vận mệnh theo Ngũ đế"); window.geometry('400x50+100+200')
      lbl = Label(window, text="Dòng ngũ đế của bạn: "); lbl.grid(column=0, row=0)                   
      value = Combobox(window); value['values']=ngude; value.grid(column=1, row=0)
      btn = Button(window, text="Xác nhận", command=clicked)
      btn.grid(column=2, row=0); btn.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def saoHan1(self):
      def info():
         mbox.showwarning(gt, "- Những thống kê và chiêm nghiệm thực tiễn cho thấy những năm sao hạn như Thái Bạch, La Hầu, Kế Đô,... ứng với chu kỳ sinh học của \
từng người. Đó là những chu kỳ \"thoái trào\", biểu hiện qua tình trạng sức khoẻ trục trặc, tâm lý thiếu sáng suốt,...\
\n- Không bao giờ vận hạn con người phải trải qua 2,3 năm xấu. Các sao xấu, tốt đan xen nhau từng năm ứng với chu kỳ sinh học của cơ thể, ảnh hưởng đến hệ \
tuần hoàn, tim mạch, tiêu hoá, tiết niệu,...\n- Về phần hạn thì tất cả đều xấu, tuy nhiên nó còn phụ thuộc vào cung Bát quái, mệnh Ngũ hành của mỗi cá nhân")
      def help():
         mbox.showwarning(hd, hdas)
      def clicked():
         x = int(spin.get())
         if x in sao1 and var.get()==1 or x in sao6 and var.get()==0:
            mbox.showinfo("Sao","La Hầu: sao xấu, chủ mồm miệng, cửa quan, tai mắt, máu huyết sản nạn, buồn rầu")
         elif x in sao2 and var.get()==1 or x in sao5 and var.get()==0:
            mbox.showinfo("Sao","Thổ Tú: sao trung bình, chủ tiểu nhân, xuất hành không thuận, nhà cửa không vui, chăn nuôi thua lỗ")
         elif x in sao3 and var.get()==1 or x in sao9 and var.get()==0:
            mbox.showinfo("Sao","Thủy Diệu: sao trung bình, chủ Tài, Lộc, Hỷ; chủ phòng việc đi sông nước và điều ăn tiếng nói")
         elif x in sao4 and var.get()==1 or x in sao8 and var.get()==0:
            mbox.showinfo("Sao","Thái Bạch: sao xấu, hao tán tiền của, tiểu nhân, kiện tụng, bệnh nội tạng")
         elif x in sao5 and var.get()==1 or x in sao7 and var.get()==0:
            mbox.showinfo("Sao","Thái Dương: sao tốt, chủ hưng vượng tài lộc")
         elif x in sao6 and var.get()==1 or x in sao2 and var.get()==0:
            mbox.showinfo("Sao","Vân Hán: sao trung bình, chủ sự thủ cựu; phòng thương tật, ốm đau, sản nạn, nóng nảy, mồm miệng, kiện tụng, giấy tờ")
         elif x in sao7 and var.get()==1 or x in sao1 and var.get()==0:
            mbox.showinfo("Sao","Kế Đô: sao xấu, chủ hung dữ, ám muội, thị phi, buồn rầu")
         elif x in sao8 and var.get()==1 or x in sao4 and var.get()==0:
            mbox.showinfo("Sao","Thái Âm: sao tốt, chủ sự toại nguyện về danh lợi; riêng nữ phòng ốm đau, tật ách, sản nạn")
         elif x in sao9 and var.get()==1 or x in sao3 and var.get()==0:
            mbox.showinfo("Sao","Mộc Đức: sao tốt, chủ hướng tới sự an vui hoà hợp")
         else:
            mbox.showerror("Lỗi",e+"\n(lưu ý: độ tuổi yêu cầu chỉ từ 10-99)")        
         if x in han1 and var.get()==1 or x in han3 and var.get()==0:
            mbox.showinfo("Hạn","Tam Kheo: đau mắt, đề phòng tai nạn chân tay")
         elif x in han2:
            mbox.showinfo("Hạn","Ngũ Hộ: hao tài")
         elif x in han3 and var.get()==1 or x in han1 and var.get()==0:
            mbox.showinfo("Hạn","Thiên Tinh: kiện tụng, lao tù")
         elif x in han4 and var.get()==1 or x in han8 and var.get()==0:
            mbox.showinfo("Hạn","Toán Tận: gặp nạn bất ngờ")
         elif x in han5 and var.get()==1 or x in han7 and var.get()==0:
            mbox.showinfo("Hạn","Thiên La: bệnh tật")
         elif x in han6:
            mbox.showinfo("Hạn","Địa Võng: nhiều chuyện buồn, thị phi")
         elif x in han7 and var.get()==1 or x in han6 and var.get()==0:
            mbox.showinfo("Hạn","Diêm Vương: không tốt đối với phụ nữ, nhất là khi sinh đẻ")
         elif x in han8 and var.get()==1 or x in han4 and var.get()==0:
            mbox.showinfo("Hạn","Huỳnh Tuyền: bệnh nặng nguy hiểm")
         else:
            mbox.showerror("Lỗi",e+"\n(lưu ý: độ tuổi yêu cầu chỉ từ 10-99)")
      info()
      window = Toplevel()
      global var; var = IntVar()
      window.title("Xem sao, xem hạn"); window.geometry('600x50+100+200')
      lbl = Label(window, text="Số tuổi của bạn:"); lbl.grid(column=0, row=0); lbl = Label(window, text="Giới tính của bạn:"); lbl.grid(column=2, row=0)      
      spin = Spinbox(window, fg="blue", font=12, from_=10, to=99, width=10); spin.grid(column=1,row=0)
      rad1 = Radiobutton(window,text='Nam', value=1, variable=var); rad1.grid(column=3, row=0)
      rad2 = Radiobutton(window,text='Nữ', value=0, variable=var); rad2.grid(column=4, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=5, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def saoHan2(self):
      def info():
         mbox.showwarning(ct, "Có thể thay thế việc cúng sao hạn bằng việc cẩn trọng trong mọi hoạt động, giữ cho tâm hồn thuần hậu, nhân hoà thì cũng có \
khả năng vượt qua những khó khăn hoạn nạn giống như người gặp lạnh thì mặc áo ấm, nóng thì mặc ít áo đi...")
      def help():
         mbox.showwarning(hd, hdas)   
      def clicked():
         x = int(spin.get())
         if x<10 or x>99:
            mbox.showerror("Lỗi",e+"\n(lưu ý: độ tuổi yêu cầu chỉ từ 10-99)")
         elif x in sao1 and var.get()==1 or x in sao6 and var.get()==0:
            bv="Thiên Cung Thần Thủ La Hầu (giấy vàng)"
            k="Cung thỉnh: Thiên cung Thần Thủ La Hầu, Thần Thủ tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 8, từ 21 đến 23 giờ, thắp 9 ngọn đèn hướng Bắc làm lễ"
         elif x in sao2 and var.get()==1 or x in sao5 and var.get()==0:
            bv="Trung ương Mậu Kỷ Thổ Đức tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Hoàng Trung Đại Thánh Thổ Địa, Địa La Thổ Tú tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 19, từ 19 đến 21 giờ, thắp 5 ngọn đèn hướng Tây làm lễ"
         elif x in sao3 and var.get()==1 or x in sao9 and var.get()==0:
            bv="Bắc phương Nhâm Quý Thuỷ Đức tinh quân (giấy đen)"
            k="Cung thỉnh: Thiên đình Thuỷ Đức Kim Nữ cung, Đại Thánh Nhâm Quý Thuỷ Diêm tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 21, từ 21 đến 23 giờ, thắp 7 ngọn đèn hướng Bắc làm lễ"
         elif x in sao4 and var.get()==1 or x in sao8 and var.get()==0:
            bv="Tây phương Canh Tân Kim Đức Thái Bạch tinh quân (giấy trắng)"
            k="Cung thỉnh: Thiên đình Hạc Linh cung Đại Thánh Kim Đức Thái Bạch tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 15, từ 21 đến 23 giờ, thắp 8 ngọn đèn hướng Tây làm lễ"
         elif x in sao5 and var.get()==1 or x in sao7 and var.get()==0:
            bv="Nhật cung Thái Dương Thiên Tử tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Uất Ly cung Đại Thánh Đang Nguyên Hải, Nhật cung Thái Dương tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 27, từ 21 đến 23 giờ, thắp 12 ngọn đèn hướng chính Đông làm lễ"
         elif x in sao6 and var.get()==1 or x in sao2 and var.get()==0:
            bv="Nam phương Bính Đinh Hoả Đức tinh quân (giấy hồng)"
            k="Cung thỉnh: Thiên đình Minh Ly cung Đại Thánh Hoả Đức Vân Hán tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 15, từ 21 đến 23 giờ, thắp 8 ngọn đèn hướng Tây làm lễ"
         elif x in sao7 and var.get()==1 or x in sao1 and var.get()==0:
            bv="Thiên Cung Thần Vĩ Kế Đô tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Bảo Vĩ cung Đại Thánh, Thần Vĩ Kế Đô tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 18, từ 21 đến 23 giờ, thắp 21 ngọn đèn hướng Tây làm lễ"
         elif x in sao8 and var.get()==1 or x in sao4 and var.get()==0:
            bv="Nguyệt Cung Thái Âm Hoàng Hậu tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Kết Lâu cung Đại Thánh, Tổ Diệu Nguyệt Phu Thái Âm tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 26, từ 19 đến 21 giờ, thắp 7 ngọn đèn hướng Tây làm lễ"
         else:
            bv="Đông phương Giáp Ất Mộc Đức tinh quân (giấy xanh)"
            k="Cung thỉnh: Thiên đình Thánh Vân cung Đại Thánh Trùng Quan Triều Nguyên Mộc Đức tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 25, từ 19 đến 21 giờ, thắp 20 ngọn đèn hướng Đông làm lễ"
         mbox.showinfo(kq,"- Bài vị: "+bv+"\n- Cách khấn:\n"+k+"\n- Cách cúng: "+cc)
      info()
      window = Toplevel()
      global var; var = IntVar()
      window.title("Cách tiễn sao xấu và nghênh sao tốt"); window.geometry('600x50+100+200')
      lbl = Label(window, text="Số tuổi của bạn:"); lbl.grid(column=0, row=0); lbl = Label(window, text="Giới tính của bạn:"); lbl.grid(column=2, row=0)      
      spin = Spinbox(window, fg="blue", font=12, from_=10, to=99, width=10); spin.grid(column=1,row=0)
      rad1 = Radiobutton(window,text='Nam', value=1, variable=var); rad1.grid(column=3, row=0)
      rad2 = Radiobutton(window,text='Nữ', value=0, variable=var); rad2.grid(column=4, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=5, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def saoHan3(self):
      def info():
         mbox.showwarning(ct, "Sơ đồ bày đèn cúng sao")
      def help():
         mbox.showwarning(hd, hdas)
      def clicked():
         if gt1.current()<10 or gt1.current()>99 or gt2.current()<0 or gt2.current()>1:
            mbox.showerror("Lỗi",e+"\n(lưu ý: độ tuổi yêu cầu chỉ từ 10-99)")
         elif gt1.current() in sao1 and gt2.current()==0 or gt1.current() in sao6 and gt2.current()==1:
            mbox.showinfo(kq,"★     ★\n★     ★\n      ★\n     ★\n★\n  ★\n     ★")
         elif gt1.current() in sao2 and gt2.current()==0 or gt1.current() in sao5 and gt2.current()==1:
            mbox.showinfo(kq,"    ★\n★ ★ ★\n    ★")
         elif gt1.current() in sao3 and gt2.current()==0 or gt1.current() in sao9 and gt2.current()==1:
            mbox.showinfo(kq,"\t\t    *  \n\t\t  *   *\n\t\t    *  \n\t\t  *   *\n\t\t    *  ")
         elif gt1.current() in sao4 and gt2.current()==0 or gt1.current() in sao8 and gt2.current()==1:
            mbox.showinfo(kq,"\t\t    *  *\n\t\t    *  *\n\t\t    *  *\n\t\t    *  *\n\t\t")
         elif gt1.current() in sao5 and gt2.current()==0 or gt1.current() in sao7 and gt2.current()==1:
            mbox.showinfo(kq,"\t\t * * * *\n\t\t * * * *\n\t\t *     *\n\t\t *     *")
         elif gt1.current() in sao6 and gt2.current()==0 or gt1.current() in sao2 and gt2.current()==1:
            mbox.showinfo(kq,"\t\t * * *\n\t\t *\n\t\t * * *\n\t\t * * *\n\t\t * * *\n\t\t   * *")
         elif gt1.current() in sao7 and gt2.current()==0 or gt1.current() in sao1 and gt2.current()==1:
            mbox.showinfo(kq,"\t\t    *\n\t\t* *   * *\n\t\t* *   * *\n\t\t* *   * *\n\t\t* *   * *\n\t\t  *   *\n\t\t  *   *")
         elif gt1.current() in sao8 and gt2.current()==0 or gt1.current() in sao4 and gt2.current()==1:
            mbox.showinfo(kq,"\t\t  *   *\n\t\t  *   *\n\t\t    *\n\t\t  *\n\t\t    *")
         else:
            mbox.showinfo(kq,"\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *\n\t\t    *\n\t\t       *\n\t\t    *\n\t\t *")
      window = Toplevel()
      global var; var = IntVar()
      window.title("Cửu diệu tinh (sơ đồ bày đèn cúng sao)"); window.geometry('600x50+100+200')
      lbl = Label(window, text="Số tuổi của bạn:"); lbl.grid(column=0, row=0); lbl = Label(window, text="Giới tính của bạn:"); lbl.grid(column=2, row=0)      
      spin = Spinbox(window, fg="blue", font=12, from_=10, to=99, width=10); spin.grid(column=1,row=0)
      rad1 = Radiobutton(window,text='Nam', value=1, variable=var); rad1.grid(column=3, row=0)
      rad2 = Radiobutton(window,text='Nữ', value=0, variable=var); rad2.grid(column=4, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=5, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def hungTai(self):
      def info():
         mbox.showwarning(kn, "Hung niên, tam tai là gì?\
      \n- Hung niên, tam tai là những năm rơi vào sao chiếu mệnh không có lợi, đặc biệt về việc hôn nhân, cưới gả và cất nhà, xây dựng nhà cửa.\
      \n- Hung niên: chớ lập gia đình, thận trọng trong việc giao dịch kinh doanh. Tiến hành cất nhà ở tuổi này cũng được nhưng không tốt lắm.\
      \n- Tam tai: kỵ cất nhà và cưới gả (năm tam tai thường là của tuổi con trai, tuổi con gái thì không sao vì phần làm nhà là phần của người nam.")
      def help():
         mbox.showwarning(hd, hddc)
      def clicked():
         hn="- Tuổi hung niên: "; tt="\n- Năm tam tai: "
         if value.current()==0:
            mbox.showinfo(kq,hn+"Măo"+tt+"Dần, Măo, Thìn")
         elif value.current()==1:
            mbox.showinfo(kq,hn+"Sửu"+tt+"Hợi, Tý, Sửu")
         elif value.current()==2:
            mbox.showinfo(kq,"- Tuổi hung niên: Thân\n- Năm tam tai: Thân, Dậu, Tuất")
         elif value.current()==3:
            mbox.showinfo(kq,"- Tuổi hung niên: Dậu\n- Năm tam tai: Tỵ, Ngọ, Mùi")         
         elif value.current()==4:
            mbox.showinfo(kq,"- Tuổi hung niên: Thìn\n- Năm tam tai: Dần, Măo, Thìn")
         elif value.current()==5:
            mbox.showinfo(kq,"- Tuổi hung niên: Hợi\n- Năm tam tai: Hợi, Tý, Sửu")
         elif value.current()==6:
            mbox.showinfo(kq,"- Tuổi hung niên: Dậu\n- Năm tam tai: Thân, Dậu, Tuất")
         elif value.current()==7:
            mbox.showinfo(kq,"- Tuổi hung niên: Tuất\n- Năm tam tai: Tỵ, Ngọ, Mùi")                  
         elif value.current()==8:
            mbox.showinfo(kq,"- Tuổi hung niên: Dần\n- Năm tam tai: Dần, Măo, Thìn")
         elif value.current()==9:
            mbox.showinfo(kq,"- Tuổi hung niên: Tý\n- Năm tam tai: Hợi, Tý, Sửu")
         elif value.current()==10:
            mbox.showinfo(kq,"- Tuổi hung niên: Tuất\n- Năm tam tai: Thân, Dậu, Tuất")
         elif value.current()==11:
            mbox.showinfo(kq,"- Tuổi hung niên: Hợi\n- Năm tam tai: Tỵ, Ngọ, Mùi")
      info()
      window = Toplevel() 
      window.title("Hung niên, tam tai"); window.geometry('400x50+200+200')
      lbl=Label(window, text="Địa chi (con giáp) của bạn:"); lbl.grid(column=0, row=0)      
      value = Combobox(window); value['values']=chi; value.grid(column=1, row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()
   def vanMenh1(self):
      def help():
         mbox.showwarning(hd, hdal1)
      def clicked1():
         r=int(spin.get())%60; s = "- Số may mắn là: "; hm = "\n- Hợp màu: "; km = "\n- Kỵ màu: "
         if r==0 or r==31:
            mbox.showinfo(kq, s+"1, 3, 6, 8\n- Hợp màu: đen, xanh\n- Kỵ màu: vàng, đỏ, trắng")
         elif r==1 or r==9 or r==38 or r==39 or r==53:
            mbox.showinfo(kq, "- Số may mắn là: 1, 6\n- Hợp màu: đen, xanh\n- Kỵ màu: vàng, đỏ, trắng")
         elif r==2 or r==3 or r==25 or r==32 or r==33:
            mbox.showinfo(kq, "- Số may mắn là: 4, 9\n- Hợp màu: trắng, đen, xanh\n- Kỵ màu: vàng, đỏ")
         elif r==4:
            mbox.showinfo(kq, "- Số may mắn là: 2, 9\n- Hợp màu: vàng, trắng\n- Kỵ màu: đỏ, xanh, đen")
         elif r==5 or r==30 or r==54:
            mbox.showinfo(kq, "- Số may mắn là: 5\n- Hợp màu: vàng, trắng\n- Kỵ màu: đỏ, xanh, đen")
         elif r==6:
            mbox.showinfo(kq, s+"1"+hm+"xanh, đỏ"+km+"vàng, trắng, đen")
         elif r==7 or r==14 or r==22 or r==28 or r==59:
            mbox.showinfo(kq, s+"2, 3, 7, 8"+hm+"xanh, đen"+km+"vàng, trắng, đỏ")
         elif r==10 or r==19 or r==40 or r==48:
            mbox.showinfo(kq, s+"2, 5, 7"+hm+"xanh, đen"+km+"vàng, trắng, đỏ")
         elif r==11:
            mbox.showinfo(kq, s+"0, 2, 5, 7"+hm+"đỏ, vàng"+km+"xanh, trắng, đen")
         elif r==12 or r==18 or r==42:
            mbox.showinfo(kq, s+"9"+hm+"vàng, trắng"+km+"xanh, đỏ, đen")
         elif r==13 or r==15 or r==23 or r==29 or r==37 or r==44 or r==45:
            mbox.showinfo(kq, s+"3, 8"+hm+"vàng, trắng"+km+"xanh, đỏ, đen")
         elif r==16:
            mbox.showinfo(kq, s+"3, 8"+hm+"trắng, đen"+km+"đỏ, xanh, vàng")
         elif r==17 or r==25 or r==32 or r==33:
            mbox.showinfo(kq, s+"4, 9"+hm+"trắng, đen"+km+"đỏ, xanh, vàng")
         elif r==20:
            mbox.showinfo(kq, s+"0, 5, 6, 9"+hm+"vàng, trắng"+km+"xanh, đỏ, đen")
         elif r==43:
            mbox.showinfo(kq, s+"4, 5, 9"+hm+"trắng, đen"+km+"đỏ, xanh, vàng")
         elif r==24 or r==46 or r==47 or r==55:
            mbox.showinfo(kq, s+"1, 4, 6, 9"+hm+"trắng, đen"+km+"đỏ, xanh, vàng")
         elif r==26 or r==41 or r==49 or r==56 or r==57:
            mbox.showinfo(kq, s+"2, 7"+hm+"đỏ, vàng"+km+"xanh, trắng, đen")
         elif r==27:
            mbox.showinfo(kq, s+"3, 7"+hm+"đỏ, vàng"+km+"xanh, trắng, đen")
         elif r==34:
            mbox.showinfo(kq, s+"3, 6, 8, 9"+hm+"vàng, trắng"+km+"xanh, đỏ, đen")
         elif r==36:
            mbox.showinfo(kq, s+"2, 3, 7"+hm+"xanh, đỏ"+km+"vàng, trắng, đen")
         elif r==51:
            mbox.showinfo(kq, s+"0, 5"+hm+"vàng, trắng"+km+"xanh, đỏ, đen")
         elif r==52:
            mbox.showinfo(kq, s+"3, 6, 8"+hm+"xanh, đen"+km+"vàng, trắng, đỏ")
         elif r==58:
            mbox.showinfo(kq, s+"2, 9"+hm+"xanh, đỏ"+km+"vàng, trắng, đen")
         elif r==59:
            mbox.showinfo(kq, s+"2, 3, 7, 8"+hm+"xanh, đỏ"+km+"vàng, trắng, đen")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel()
      window.title("Số may mắn và màu sắc"); window.geometry('500x100+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Tra bằng năm sinh dương lịch"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Tra bằng năm sinh âm lịch"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Năm sinh dương lịch: "); lbl2 = Label(tab2, text="Năm sinh âm lịch:")
      lbl1.grid(column=0, row=0); lbl2.grid(column=0, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=9999, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=canchi; value.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn2 = Button(tab2, text="Xác nhận", command=clicked2) 
      btn1.grid(column=2, row=0); btn2.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def ngayTot(self):
      def info():
         mbox.showwarning(gt, ntnx)
      def note():
         mbox.showwarning(ct, "- Các sao làm mọi việc đều tốt:\n+ Thiên đức\n+ Nguyệt đức (Lục hợp)\n+ Thiên giải\n+ Thiên hỷ\n+ Thiên quý (Yếu yên)\n+ Tam hợp (Ngũ \
phú)\n- Các sao khác:\n+ Sinh khí (thuận việc làm nhà, sửa nhà, động thổ)\n+ Thiên hành (cưới gả, giao dịch tốt), Thiên quan (xuất hành, giao dịch tốt)\n+ Lộc mã \
(xuất hành, di chuyển tốt)\n+ Phúc sinh (được phúc tốt)\n+ Giải thần (giải trừ các sao xấu)\n+ Thiên ân (được hưởng phúc ân, làm nhà, khai trương)...\
\n- Phương thức hiển thị kết quả:\n+ Xem theo tháng: sao/ngày âm lịch (Lộc mã: Tý)\n+ Xem theo sao: tháng âm lịch/ngày âm lịch (1: Tý)")
      def help():
         mbox.showwarning(gt, ntnx)
      def clicked1():
         x = int(spin.get())
         if x==1:
            mbox.showinfo(kq, "- Thiên đức: Tỵ\n- Nguyệt đức: Hợi\n- Thiên giải: Ngọ\n- Thiên hỷ: Tuất\n- Thiên quý: Dần\n- Tam hợp: Ngọ\n- Sinh khí: Tý\n\
- Thiên hành: Mùi\n- Thiên quan: Tuất\n- Lộc mã: Ngọ\n- Phúc sinh: Dậu\n- Giải thần: Thân\n- Thiên ân: Tuất")
         elif x==2:
            mbox.showinfo(kq, "- Thiên đức: Mùi\n- Nguyệt đức: Tuất\n- Thiên giải: Thân\n- Thiên hỷ: Hợi\n- Thiên quý: Thân\n- Tam hợp: Mùi\n- Sinh khí: Sửu\n\
- Thiên hành: Dậu\n- Thiên quan: Tý\n- Lộc mã: Thân\n- Phúc sinh: Mão\n- Giải thần: Thân\n- Thiên ân: Sửu")
         elif x==3:
            mbox.showinfo(kq, "- Thiên đức: Dậu\n- Nguyệt đức: Dậu\n- Thiên giải: Tuất\n- Thiên hỷ: Tý\n- Thiên quý: Mão\n- Tam hợp: Thân\n- Sinh khí: Dần\n\
- Thiên hành: Hợi\n- Thiên quan: Dần\n- Lộc mã: Tuất\n- Phúc sinh: Tuất\n- Giải thần: Tuất\n- Thiên ân: Dần")
         elif x==4:
            mbox.showinfo(kq, "- Thiên đức: Hợi\n- Nguyệt đức: Thân\n- Thiên giải: Tý\n- Thiên hỷ: Sửu\n- Thiên quý: Dậu\n- Tam hợp: Dậu\n- Sinh khí: Mão\n\
- Thiên hành: Sửu\n- Thiên quan: Thìn\n- Lộc mã: Tý\n- Phúc sinh: Thìn\n- Giải thần: Tuất\n- Thiên ân: Tỵ")
         elif x==5:
            mbox.showinfo(kq, "- Thiên đức: Sửu\n- Nguyệt đức: Mùi\n- Thiên giải: Dần\n- Thiên hỷ: Dần\n- Thiên quý: Thìn\n- Tam hợp: Tuất\n- Sinh khí: Thìn\n\
- Thiên hành: Mão\n- Thiên quan: Ngọ\n- Lộc mã: Dần\n- Phúc sinh: Hợi\n- Giải thần: Tý\n- Thiên ân: Dậu")
         elif x==6:
            mbox.showinfo(kq, "- Thiên đức: Mão\n- Nguyệt đức: Ngọ\n- Thiên giải: Thìn\n- Thiên hỷ: Mão\n- Thiên quý: Tuất\n- Tam hợp: Hợi\n- Sinh khí: Tỵ\n\
- Thiên hành: Tỵ\n- Thiên quan: Thân\n- Lộc mã: Thìn\n- Phúc sinh: Tỵ\n- Giải thần: Tý\n- Thiên ân: Mão")
         elif x==7:
            mbox.showinfo(kq, "- Thiên đức: Tỵ\n- Nguyệt đức: Tỵ\n- Thiên giải: Ngọ\n- Thiên hỷ: Thìn\n- Thiên quý: Tỵ\n- Tam hợp: Tý\n- Sinh khí: Ngọ\n\
- Thiên hành: Mùi\n- Thiên quan: Tuất\n- Lộc mã: Ngọ\n- Phúc sinh: Tý\n- Giải thần: Dần\n- Thiên ân: Tý")
         elif x==8:
            mbox.showinfo(kq, "- Thiên đức: Mùi\n- Nguyệt đức: Thìn\n- Thiên giải: Thân\n- Thiên hỷ: Tỵ\n- Thiên quý: Hợi\n- Tam hợp: Sửu\n- Sinh khí: Mùi\n\
- Thiên hành: Dậu\n- Thiên quan: Tý\n- Lộc mã: Thân\n- Phúc sinh: Ngọ\n- Giải thần: Dần\n- Thiên ân: Ngọ")
         elif x==9:
            mbox.showinfo(kq, "- Thiên đức: Dậu\n- Nguyệt đức: Mão\n- Thiên giải: Tuất\n- Thiên hỷ: Ngọ\n- Thiên quý: Ngọ\n- Tam hợp: Dần\n- Sinh khí: Thân\n\
- Thiên hành: Hợi\n- Thiên quan: Dần\n- Lộc mã: Tuất\n- Phúc sinh: Sửu\n- Giải thần: Thìn\n- Thiên ân: Thân")
         elif x==10:
            mbox.showinfo(kq, "- Thiên đức: Hợi\n- Nguyệt đức: Dần\n- Thiên giải: Tý\n- Thiên hỷ: Mùi\n- Thiên quý: Tý\n- Tam hợp: Mão\n- Sinh khí: Dậu\n\
- Thiên hành: Sửu\n- Thiên quan: Thìn\n- Lộc mã: Tý\n- Phúc sinh: Mùi\n- Giải thần: Thìn\n- Thiên ân: Thìn")
         elif x==11:
            mbox.showinfo(kq, "- Thiên đức: Sửu\n- Nguyệt đức: Sửu\n- Thiên giải: Dần\n- Thiên hỷ: Thân\n- Thiên quý: Mùi\n- Tam hợp: Thìn\n- Sinh khí: Tuất\n\
- Thiên hành: Mão\n- Thiên quan: Ngọ\n- Lộc mã: Dần\n- Phúc sinh: Dần\n- Giải thần: Ngọ\n- Thiên ân: Thân")
         elif x==12:
            mbox.showinfo(kq, "- Thiên đức: Mão\n- Nguyệt đức: Tý\n- Thiên giải: Thìn\n- Thiên hỷ: Dậu\n- Thiên quý: Sửu\n- Tam hợp: Tỵ\n- Sinh khí: Hợi\n\
- Thiên hành: Tỵ\n- Thiên quan: Thân\n- Lộc mã: Thìn\n- Phúc sinh: Thân\n- Giải thần: Ngọ\n- Thiên ân: Mùi")
         else:
            mbox.showerror("Lỗi",e)
      def clicked2():
         x = value.current()
         if x==0:
            mbox.showinfo(kq, "- 1: Tỵ\n- 2: Mùi\n- 3: Dậu\n- 4: Hợi\n- 5: Sửu\n- 6: Mão\n- 7: Tỵ\n- 8: Mùi\n- 9: Dậu\n- 10: Hợi\n- 11: Sửu\n- 12: Mão")
         elif x==1:
            mbox.showinfo(kq, "- 1: Hợi\n- 2: Tuất\n- 3: Dậu\n- 4: Thân\n- 5: Mùi\n- 6: Ngọ\n- 7: Tỵ\n- 8: Thìn\n- 9: Mão\n- 10: Dần\n- 11: Sửu\n- 12: Tý")
         elif x==2 or x==9:
            mbox.showinfo(kq, "- 1: Ngọ\n- 2: Thân\n- 3: Tuất\n- 4: Tý\n- 5: Dần\n- 6: Thìn\n- 7: Ngọ\n- 8: Thân\n- 9: Tuất\n- 10: Tý\n- 11: Dần\n- 12: Thìn")
         elif x==3:
            mbox.showinfo(kq, "- 1: Tuất\n- 2: Hợi\n- 3: Tý\n- 4: Sửu\n- 5: Dần\n- 6: Mão\n- 7: Thìn\n- 8: Tỵ\n- 9: Ngọ\n- 10: Mùi\n- 11: Thân\n- 12: Dậu")
         elif x==4:
            mbox.showinfo(kq, "- 1: Dần\n- 2: Thân\n- 3: Mão\n- 4: Dậu\n- 5: Thìn\n- 6: Tuất\n- 7: Tỵ\n- 8: Hợi\n- 9: Ngọ\n- 10: Tý\n- 11: Mùi\n- 12: Sửu")
         elif x==5:
            mbox.showinfo(kq, "- 1: Ngọ\n- 2: Mùi\n- 3: Thân\n- 4: Dậu\n- 5: Tuất\n- 6: Hợi\n- 7: Tý\n- 8: Sửu\n- 9: Dần\n- 10: Mão\n- 11: Thìn\n- 12: Tỵ")
         elif x==6:
            mbox.showinfo(kq, "- 1: Tý\n- 2: Sửu\n- 3: Dần\n- 4: Mão\n- 5: Thìn\n- 6: Tỵ\n- 7: Ngọ\n- 8: Mùi\n- 9: Thân\n- 10: Dậu\n- 11: Tuất\n- 12: Hợi")
         elif x==7:
            mbox.showinfo(kq, "- 1: Mùi\n- 2: Dậu\n- 3: Hợi\n- 4: Sửu\n- 5: Mão\n- 6: Tỵ\n- 7: Mùi\n- 8: Dậu\n- 9: Hợi\n- 10: Sửu\n- 11: Mão\n- 12: Tỵ")
         elif x==8:
            mbox.showinfo(kq, "- 1: Tuất\n- 2: Tý\n- 3: Dần\n- 4: Thìn\n- 5: Ngọ\n- 6: Thân\n- 7: Tuất\n- 8: Tý\n- 9: Dần\n- 10: Thìn\n- 11: Ngọ\n- 12: Thân")
         elif x==10:
            mbox.showinfo(kq, "- 1: Dậu\n- 2: Mão\n- 3: Tuất\n- 4: Thìn\n- 5: Hợi\n- 6: Tỵ\n- 7: Tý\n- 8: Ngọ\n- 9: Sửu\n- 10: Mùi\n- 11: Dần\n- 12: Thân")
         elif x==11:
            mbox.showinfo(kq, "- 1: Thân\n- 2: Thân\n- 3: Tuất\n- 4: Tuất\n- 5: Tý\n- 6: Tý\n- 7: Dần\n- 8: Dần\n- 9: Thìn\n- 10: Thìn\n- 11: Ngọ\n- 12: Ngọ")
         elif x==12:
            mbox.showinfo(kq, "- 1: Tuất\n- 2: Sửu\n- 3: Dần\n- 4: Tỵ\n- 5: Dậu\n- 6: Mão\n- 7: Tý\n- 8: Ngọ\n- 9: Thân\n- 10: Thìn\n- 11: Thân\n- 12: Mùi")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Ngày tốt"); window.geometry('500x50+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Xem theo tháng"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Xem theo sao"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Tháng âm lịch: "); lbl1.grid(column=0, row=0); lbl1 = Label(tab1, text="(sao: ngày âm lịch)"); lbl1.grid(column=3, row=0)
      lbl2 = Label(tab2, text="Sao:"); lbl2.grid(column=0, row=0); lbl2 = Label(tab2, text="(tháng âm lịch: ngày âm lịch)"); lbl2.grid(column=3, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=12, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=saotot; value.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn1.grid(column=2, row=0)
      btn2 = Button(tab2, text="Xác nhận", command=clicked2); btn2.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=ct, command=note); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def ngayXau(self):
      def info():
         mbox.showwarning(gt, ntnx)
      def note():
         mbox.showwarning(ct, "- Mỗi tháng có ba ngày Nguyệt kỵ: 5, 14, 23 và 6 ngày Tam nương: 3, 7, 13, 18, 22, 27. Ngoài ra mỗi năm còn có 13 ngày Dương công (xấu)\
:\n+ 13 tháng 1\n+ 12 tháng 2\n+ 9 tháng 3\n+ 7 tháng 4\n+ 5 tháng 5\n+ 3 tháng 6\n+ 8 và 29 tháng 7\n+ 27 tháng 8\n+ 25 tháng 9\n+ 23 tháng 10\n+ 21 tháng 11\n+ 19 \
tháng 12\n(lưu ý: tất cả đều được tính theo ngày tháng Âm lịch)\n- Ngoài ra còn có các sao xấu khác:\n+ Thiên cương\n+ Thụ tử\n+ Đại hao\n+ Tử khí\n+ Quan phù (xấu trong \
mọi việc lớn)\n+ Tiểu hao (kỵ xuất nhập, tiền tài)\n+ Sát chủ\n+ Thiên hoả\n+ Địa hoả\n+ Hoả tai\n+ Nguyệt phá (kiêng làm nhà)\n+ Băng tiêu ngoạ giải (kiêng làm nhà \
và mọi việc lớn)\n+ Thổ cấm (kiêng động thổ)\n+ Thổ kỵ (kỵ động thổ)\n+ Vãng vong (kiêng xuất hành, giá thú)\n+ Cô thân\n+ Quả tú (kiêng giá thú)\n+ Trùng tang\n+ \
Trùng phục (kỵ hôn nhân, mai táng, cải táng)\n- Phương thức hiển thị kết quả:\n+ Xem theo tháng: sao/ngày âm lịch (Thụ tử: Tý)\n+ Xem theo sao: tháng âm lịch/ngày \
âm lịch (1: Tý)")
      def help():
         mbox.showwarning(gt, hdal2+" hoặc "+hds)
      def clicked1():
         x = int(spin.get())
      def clicked2():
         x = value.current()
         if x==0:
            mbox.showinfo(kq, "- 1: Tỵ\n- 2: Tý\n- 3: Mùi\n- 4: Dần\n- 5: Dậu\n- 6: Thìn\n- 7: Hợi\n- 8: Ngọ\n- 9: Sửu\n- 10: Thân\n- 11: Mão\n- 12: Tuất")
         elif x==1:
            mbox.showinfo(kq, "- 1: Tuất\n- 2: Thìn\n- 3: Hợi\n- 4: Tỵ\n- 5: Tý\n- 6: Ngọ\n- 7: Sửu\n- 8: Mùi\n- 9: Dần\n- 10: Thân\n- 11: Mão\n- 12: Dậu") ####
         elif x==2 or x==3 or x==4:
            mbox.showinfo(kq, "- 1: Ngọ\n- 2: Mùi\n- 3: Thân\n- 4: Dậu\n- 5: Tuất\n- 6: Hợi\n- 7: Tý\n- 8: Sửu\n- 9: Dần\n- 10: Mão\n- 11: Thìn\n- 12: Tỵ")
         elif x==5:
            mbox.showinfo(kq, "- 1: Tỵ\n- 2: Ngọ\n- 3: Mùi\n- 4: Thân\n- 5: Dậu\n- 6: Tuất\n- 7: Hợi\n- 8: Tý\n- 9: Sửu\n- 10: Dần\n- 11: Mão\n- 12: Thìn")
         elif x==6:
            mbox.showinfo(kq, "- 1: Tỵ\n- 2: Tý\n- 3: Mùi\n- 4: Mão\n- 5: Thân\n- 6: Tuất\n- 7: Sửu\n- 8: Hợi\n- 9: Ngọ\n- 10: Dậu\n- 11: Dần\n- 12: Thìn")
         elif x==7:
            mbox.showinfo(kq, "- 1: Tý\n- 2: Mão\n- 3: Ngọ\n- 4: Dậu\n- 5: Tý\n- 6: Mão\n- 7: Ngọ\n- 8: Dậu\n- 9: Tý\n- 10: Mão\n- 11: Ngọ\n- 12: Dậu")
         elif x==8:
            mbox.showinfo(kq, "- 1: Tuất\n- 2: Dậu\n- 3: Thân\n- 4: Mùi\n- 5: Ngọ\n- 6: Tỵ\n- 7: Thìn\n- 8: Mão\n- 9: Dần\n- 10: Sửu\n- 11: Tý\n- 12: Hợi")
         elif x==9:
            mbox.showinfo(kq, "- 1: Sửu\n- 2: Mùi\n- 3: Dần\n- 4: Thân\n- 5: Mão\n- 6: Dậu\n- 7: Thìn\n- 8: Tuất\n- 9: Tỵ\n- 10: Hợi\n- 11: Tý\n- 12: Ngọ")
         elif x==10:
            mbox.showinfo(kq, "- 1: Thân\n- 2: Tuất\n- 3: Tuất\n- 4: Hợi\n- 5: Sửu\n- 6: Sửu\n- 7: Dần\n- 8: Thìn\n- 9: Thìn\n- 10: Tỵ\n- 11: Mùi\n- 12: Mùi")
         elif x==11:
            mbox.showinfo(kq, "- 1: Tỵ\n- 2: Tý\n- 3: Sửu\n- 4: Thân\n- 5: Mão\n- 6: Tuất\n- 7: Hợi\n- 8: Ngọ\n- 9: Mùi\n- 10: Dần\n- 11: Dậu\n- 12: Thìn")
         elif x==12:
            mbox.showinfo(kq, "- 1: Hợi\n- 2: Hợi\n- 3: Hợi\n- 4: Dần\n- 5: Dần\n- 6: Dần\n- 7: Tỵ\n- 8: Tỵ\n- 9: Tỵ\n- 10: Thân\n- 11: Thân\n- 12: Thân")
         elif x==13 or x==14:
            mbox.showinfo(kq, "- 1: Dần\n- 2: Tỵ\n- 3: Thân\n- 4: Hợi\n- 5: Mão\n- 6: Ngọ\n- 7: Dậu\n- 8: Tý\n- 9: Thìn\n- 10: Mùi\n- 11: Tuất\n- 12: Sửu")
         elif x==15:
            mbox.showinfo(kq, "- 1: Tuất\n- 2: Hợi\n- 3: Tý\n- 4: Sửu\n- 5: Dần\n- 6: Mão\n- 7: Thìn\n- 8: Tỵ\n- 9: Ngọ\n- 10: Mùi\n- 11: Thân\n- 12: Dậu")
         elif x==16:
            mbox.showinfo(kq, "- 1: Thìn\n- 2: Tỵ\n- 3: Ngọ\n- 4: Mùi\n- 5: Thân\n- 6: Dậu\n- 7: Tuất\n- 8: Hợi\n- 9: Tý\n- 10: Sửu\n- 11: Dần\n- 12: Mão")
         elif x==17:
            mbox.showinfo(kq, "- 1: Giáp\n- 2: Ất\n- 3: Mậu\n- 4: Bính\n- 5: Đinh\n- 6: Kỷ\n- 7: Canh\n- 8: Tân\n- 9: Kỷ\n- 10: Nhâm\n- 11: Quý\n- 12: Mậu")
         elif x==18:
            mbox.showinfo(kq, "- 1: Canh\n- 2: Tân\n- 3: Kỷ\n- 4: Nhâm\n- 5: Quý\n- 6: Mậu\n- 7: Giáp\n- 8: Ất\n- 9: Kỷ\n- 10: Bính\n- 11: Đinh\n- 12: Mậu")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Ngày xấu"); window.geometry('500x50+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Xem theo tháng"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Xem theo sao"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Tháng âm lịch: "); lbl1.grid(column=0, row=0); lbl1 = Label(tab1, text="(sao: ngày âm lịch)"); lbl1.grid(column=3, row=0)
      lbl2 = Label(tab2, text="Sao:"); lbl2.grid(column=0, row=0); lbl2 = Label(tab2, text="(tháng âm lịch: ngày âm lịch)"); lbl2.grid(column=3, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=12, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=saoxau; value.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn1.grid(column=2, row=0)
      btn2 = Button(tab2, text="Xác nhận", command=clicked2); btn2.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=ct, command=note); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def ngayTiet(self):
      def info():
         mbox.showwarning(kn, "- Tứ ly và Tứ tuyệt được gọi chung là ngày Tứ lập. Đây là những ngày thiên nhiên, trời đất giao hòa, bạn cần tránh làm những việc ảnh \
hưởng tới âm dương, ngũ hành…\n- Trong 12 tiết khí, cổ nhân coi ngày Lập Xuân, Lập Hạ, Lập Thu, Lập Đông là Tứ lập. Ngày trước Lập Xuân, Lập Hạ, Lập Thu, Lập Đông một \
ngày là ngày Tứ tuyệt. Tên gọi là Tứ tuyệt là bởi bạn cần đó là 4 ngày kết thúc, tận cùng của 1 mùa, rất không tốt cho xuất hành, kết hôn…\n- Bên cạnh đó, ngày trước \
Xuân Phân, Hạ Chí, Thu Phân, Đông Chí một ngày là Tứ Ly. Tên gọi của các ngày lần lượt là Mộc Ly, Hỏa Ly, Kim Ly, Hỏa Ly. Đây là thời điểm phân chia mùa, âm dương, \
ngũ hành không cân bằng nên hạn chế việc khai trương xuất hành…\n- Những lưu ý trong ngày Tứ ly, Tứ tuyệt. Ngày Tứ lập được dân gian coi là ngày giao mùa. Vạn vật \
sinh linh đều nằm trạng thái giao thoa và có sự va chạm bất ổn. Vào ngày tiết mùa giao thoa, hành vi con người nên thuận theo thiên đạo. Tu thần dưỡng tính, điều \
tiết tâm tình, duy trì trạng thái tâm an, cơ thể nghỉ ngơi. Tinh thần thì thu về, khiêm nhường; tránh phóng thích tinh hoa. Vậy nên mới có truyền thuyết, ngày Tứ ly \
Tứ tuyệt kỵ phòng the, tất thêm 3 năm dương thọ...")
      def help():
         mbox.showwarning(hd, hddl1)
      def clicked():
         y = int(spin.get())
         if y%4==0:
            mbox.showinfo(kq, "- 4 ngày Tứ ly: 21/3, 21/6, 23/9 và 22/12\n- 4 ngày Tứ tuyệt: 4/2, 6/5, 8/8 và 7/11")
         elif y%4!=0:
            mbox.showinfo(kq, "- 4 ngày Tứ ly: 20/3, 20/6, 22/9 và 21/12\n- 4 ngày Tứ tuyệt: 3/2, 5/5, 7/8 và 6/11")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Ngày tiết"); window.geometry('400x50+100+200')
      lbl = Label(window, text="Năm dương lịch: "); lbl.grid(column=0, row=0)
      spin = Spinbox(window, fg="blue", font=12, from_=1, to=9999, width=14); spin.grid(column=1,row=0) 
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)      
      window.mainloop()
   def nhiThapBatTu(self):
      def info():
         mbox.showwarning(gt, "- Các nhà Thiên văn học chia bầu trời ra 4 hướng: Đông Tây Nam Bắc. Mỗi hướng gồm có 7 chùm sao: 4 hướng x 7 chùm sao = 28 chùm sao. \
Ngày nay chúng ta thường gọi là Nhị Thập Bát Tú.\
\n- Bảy chòm sao hợp lại thành một phương trời và được biểu tượng thành một con vật có màu sắc theo sự phối thuộc của ngũ hành:\
\n+ Phương Đông là con rồng xanh, gọi là Thanh Long (Giác, Cang, Đê, Phòng, Tâm, Vĩ, Cơ), thuộc Mộc, màu xanh.\
\n+ Phương Bắc là con rùa đen gọi là Hoa Cái (Đẩu, Ngưu, Nữ, Hư, Nguy, Thất, Bích), thuộc Thủy, màu đen.\
\n+ Phương Tây là con hổ trắng gọi là Bạch Hổ (Khuê, Lâu, Vị, Mão, Tất, Chuỷ, Sâm), thuộc Kim, màu trắng.\
\n+ Phương Nam là con phượng đỏ gọi là Phượng Các (Tỉnh, Quỷ, Liễu, Tinh, Trương, Dực, Chẩn), thuộc Hỏa, màu đỏ.\
\n- Ngoài ra mỗi chòm ở mỗi phương lại có hai chòm sao ứng với bốn tháng cuối của bốn mùa, nên còn mang thêm hành Thổ, màu vàng. Đó là các sao:\
\n+ Sao Giác, Cang (thuộc Thanh Long)\n+ Sao Đẩu, Ngưu (thuộc Huyền Vũ)\n+ Sao Khuê, Lâu (thuộc Bạch Hổ)\n+ Sao Tinh, Quỷ (thuộc Chu Tước)")
      def help():
         mbox.showwarning(gt, "- Tra cứu: Chọn ngày âm lịch tại thanh trắng đầu tiên và chọn thứ phù hợp tại thanh trắng thứ hai rồi nhấn nút Xác nhận\n- Các \
mục khác: "+hds)
      def clicked1():
         x = value1.current(); y = value2.current()
         if x==2 and y==3 or x==6 and y==3 or x==10 and y==3:
            mbox.showinfo(kq, "Sao: Giác")
         elif x==2 and y==4 or x==6 and y==4 or x==10 and y==4:
            mbox.showinfo(kq, "Sao: Ngưu")
         elif x==2 and y==5 or x==6 and y==5 or x==10 and y==5:
            mbox.showinfo(kq, "Sao: Vị")
         elif x==2 and y==6 or x==y==6 or x==10 and y==6:
            mbox.showinfo(kq, "Sao: Tinh")
         elif x==2 and y==0 or x==6 and y==0 or x==10 and y==0:
            mbox.showinfo(kq, "Sao: Tâm")
         elif x==2 and y==1 or x==6 and y==1 or x==10 and y==1:
            mbox.showinfo(kq, "Sao: Thất")
         elif x==2 and y==2 or x==6 and y==2 or x==10 and y==2:
            mbox.showinfo(kq, "Sao: Sâm")
         elif x==0 and y==3 or x==4 and y==3 or x==8 and y==3:
            mbox.showinfo(kq, "Sao: Khuê")
         elif x==0 and y==4 or x==y==4 or x==8 and y==4:
            mbox.showinfo(kq, "Sao: Quỷ")
         elif x==0 and y==5 or x==4 and y==5 or x==8 and y==5:
            mbox.showinfo(kq, "Sao: Đê")
         elif x==0 and y==6 or x==4 and y==6 or x==8 and y==6:
            mbox.showinfo(kq, "Sao: Hư")
         elif x==y==0 or x==4 and y==0 or x==8 and y==0:
            mbox.showinfo(kq, "Sao: Tất")
         elif x==0 and y==1 or x==4 and y==1 or x==8 and y==1:
            mbox.showinfo(kq, "Sao: Dực")
         elif x==0 and y==2 or x==4 and y==2 or x==8 and y==2:
            mbox.showinfo(kq, "Sao: Cơ")
         elif x==1 and y==3 or x==5 and y==3 or x==10 and y==3:
            mbox.showinfo(kq, "Sao: Đẩu")
         elif x==1 and y==4 or x==5 and y==4 or x==10 and y==4:
            mbox.showinfo(kq, "Sao: Lâu")
         elif x==1 and y==5 or x==5 and y==5 or x==10 and y==5:
            mbox.showinfo(kq, "Sao: Liễu")
         elif x==1 and y==6 or x==5 and y==6 or x==10 and y==6:
            mbox.showinfo(kq, "Sao: Phòng")
         elif x==1 and y==0 or x==5 and y==0 or x==10 and y==0:
            mbox.showinfo(kq, "Sao: Nguy")
         elif x==y==1 or x==5 and y==1 or x==10 and y==1:
            mbox.showinfo(kq, "Sao: Chuỷ")
         elif x==1 and y==2 or x==5 and y==2 or x==10 and y==2:
            mbox.showinfo(kq, "Sao: Chẩn")
         elif x==y==3 or x==7 and y==3 or x==11 and y==3:
            mbox.showinfo(kq, "Sao: Tỉnh")
         elif x==3 and y==4 or x==7 and y==4 or x==11 and y==4:
            mbox.showinfo(kq, "Sao: Cang")
         elif x==3 and y==5 or x==7 and y==5 or x==11 and y==5:
            mbox.showinfo(kq, "Sao: Nữ")
         elif x==3 and y==6 or x==7 and y==6 or x==11 and y==6:
            mbox.showinfo(kq, "Sao: Mão")
         elif x==3 and y==0 or x==7 and y==0 or x==11 and y==0:
            mbox.showinfo(kq, "Sao: Trương")
         elif x==3 and y==1 or x==7 and y==1 or x==11 and y==1:
            mbox.showinfo(kq, "Sao: Vĩ")
         elif x==3 and y==2 or x==7 and y==2 or x==11 and y==2:
            mbox.showinfo(kq, "Sao: Bích")
         else:
            mbox.showerror("Lỗi",e)
      def clicked2():
         x = value3.current()
         if x<0 or x>27:
            mbox.showerror("Lỗi",e)
         elif x==0 or x==3 or x==5 or x==12 or x==13 or x==15 or x==16 or x==18 or x==25 or x==27:
            mbox.showinfo(kq, "Sao tốt: sống được bách niên giai lão, sinh quý tử, gia đình hưng vượng")
         elif x==1 or x==2 or x==4 or x==8 or x==17 or x==20 or x==22 or x==26:
            mbox.showinfo(kq, "Sao xấu: gia đình lục đục, hao tốn tiền tài, kết cuộc vợ chồng không từ biệt cũng sinh ly")
         else:
            mbox.showinfo(kq, "Sao bình thường")
      def clicked3():
         x = value4.current(); st = "Sao tốt: "; sx = "Sao xấu: "
         if x==0:
            mbox.showinfo(kq, sx+"sau ba năm sẽ bị ôn hoàng, dịch lệ")
         elif x==1 or x==2:
            mbox.showinfo(kq, sx+"quan tụng, tai hoạ liên miên")
         elif x==3:
            mbox.showinfo(kq, st+"gia đình thịnh vượng, thăng tiến")
         elif x==4:
            mbox.showinfo(kq, sx+"có tang khác tiếp liền")
         elif x==5:
            mbox.showinfo(kq, st+"con cháu đề huề, bình an")
         elif x==6:
            mbox.showinfo(kq, st+"thoả lòng người sống, an hồn người chết")
         elif x==7:
            mbox.showinfo(kq, st+"gia đình sinh phú quý")
         elif x==8 or x==10 or x==15:
            mbox.showinfo(kq, "Sao bình thường, không hại đến mai táng")
         elif x==9:
            mbox.showinfo(kq, sx+"gia đình xáo trộn, yêu quỷ phá")
         elif x==11:
            mbox.showinfo(kq, sx+"bệnh tật quanh năm")
         elif x==12:
            mbox.showinfo(kq, st+"gia đình hưng vượng, phước sẽ tới")
         elif x==13:
            mbox.showinfo(kq, st+"tài lợi tiến, quan tước thăng")
         elif x==14:
            mbox.showinfo(kq, sx+"kỵ trùng tang đến tam tang")
         elif x==16:
            mbox.showinfo(kq, st+"quan lộc tiến, tai qua nạn khỏi")
         elif x==17:
            mbox.showinfo(kq, sx+"kỵ tam tang")
         elif x==18:
            mbox.showinfo(kq, st+"gia đinh hưng vượng, thêm phú quý")
         elif x==19:
            mbox.showinfo(kq, sx+"phạm hung quái, tam tang")
         elif x==20:
            mbox.showinfo(kq, sx+"phạm tai ách, tang thương")
         elif x==21:
            mbox.showinfo(kq, sx+"phạm ôn dịch, kinh phong, ác tử")
         elif x==22:
            mbox.showinfo(kq, st+"con cháu tiến đạt công danh")
         elif x==23:
            mbox.showinfo(kq, sx+"hung tinh, gia đình sinh bệnh hoạn")
         elif x==24:
            mbox.showinfo(kq, sx+"phạm hung thần, có hại cho con gái")
         elif x==25:
            mbox.showinfo(kq, st+"gia đình hưng vượng, công danh hiển")
         elif x==26:
            mbox.showinfo(kq, sx+"phạm hoạ hại, con cháu phải ly thương")
         elif x==27:
            mbox.showinfo(kq, st+"gia đình vững bền, phát đạt")
         else:
            mbox.showerror("Lỗi",e)
      def clicked4():
         x = value5.current()
         if x<0 or x>27:
            mbox.showerror("Lỗi",e)
         elif x==0 or x==1 or x==8 or x==14 or x==15 or x==22 or x==24:
            mbox.showinfo(kq, "Thất sát tinh (sao xấu): kỵ việc khởi công, xây cất")
         else:
            mbox.showinfo(kq, "Sao bình thường")
      def list1():
         mbox.showinfo(kq, "- Sao tốt: Giác, Phòng, Vĩ, Thất, Bích, Lâu, Vị, Tất, Trương, Chẩn\n- Sao xấu: Cang, Đê, Tâm, Ngưu, Mão, Sâm, Quỷ, Dực\n- Còn lại \
các sao khác bình thường với việc hôn nhân")
      def list2():
         mbox.showinfo(kq, "- Sao tốt: Chẩn, Vĩ, Đẩu, Bích, Quỷ, Cơ, Tất, Thất, Trương, Phòng, Vị\n- Sao xấu: Tâm, Mão, Nguy, Khuê, Sâm, Chuỷ, Đê, Giác, Dực, Tinh, \
Liễu, Tỉnh, Nữ, Cang\n- Sao bình thường, không hại đến mai táng: Ngưu, Hư, Lâu")
      def list3():
         mbox.showinfo(kq, "- Thất sát tinh (sao xấu): Giác, Cang, Ngưu, Khuê, Lâu, Quỷ, Tinh\n- Còn lại các sao khác bình thường, không hại gì")
      info()
      window = Toplevel() 
      window.title("Nhị thập bát tú"); window.geometry('700x50+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control); tab3 = ttk.Frame(tab_control); tab4 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Tra cứu"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Hôn nhân"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab3, text="Mai táng"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab4, text="Xây cất, khởi công"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Ngày âm lịch: "); lbl1.grid(column=0, row=0)
      lbl2 = Label(tab1, text="Thứ: "); lbl2.grid(column=2, row=0)
      value1 = Combobox(tab1); value1['values']=chi; value1.grid(column=1, row=0)
      value2 = Combobox(tab1); value2['values']=thu; value2.grid(column=3, row=0)
      lbl2 = Label(tab2, text="Sao: "); lbl2.grid(column=0, row=0)
      lbl3 = Label(tab3, text="Sao: "); lbl3.grid(column=0, row=0)
      lbl4 = Label(tab4, text="Sao: "); lbl4.grid(column=0, row=0)
      value3 = Combobox(tab2); value3['values']=nhithapbattu; value3.grid(column=1, row=0)
      value4 = Combobox(tab3); value4['values']=nhithapbattu; value4.grid(column=1, row=0)
      value5 = Combobox(tab4); value5['values']=nhithapbattu; value5.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn1.grid(column=6, row=0)
      btn21 = Button(tab2, text="Xác nhận", command=clicked2); btn21.grid(column=2, row=0)
      btn22 = Button(tab2, text="Danh sách", command=list1); btn22.grid(column=3, row=0)
      btn31 = Button(tab3, text="Xác nhận", command=clicked3); btn31.grid(column=2, row=0)
      btn32 = Button(tab3, text="Danh sách", command=list2); btn32.grid(column=3, row=0)
      btn41 = Button(tab4, text="Xác nhận", command=clicked4); btn41.grid(column=2, row=0)
      btn42 = Button(tab4, text="Danh sách", command=list3); btn42.grid(column=3, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def hoangHac(self):
      def info():
         mbox.showwarning(kn, "Trong một tháng đều có 4 ngày Hoàng đạo và 4 ngày Hắc đạo, mỗi ngày Hoàng đạo thì sẽ lại có 6 giờ Hoàng đạo\
\n- Ngày Hoàng đạo: tốt, có thể cưới gả, chôn cất, đám tang, cải táng, làm nhà, mở cửa hàng, cửa hiệu, đi xa,...\
\n- Ngày Hắc đạo: không nên làm việc lớn, tối kỵ việc cưới gả, an táng, làm nhà, làm bếp,...\
\n- Giờ hoàng đạo: giờ tốt, giống ngày Hoàng đạo")
      def help():
         mbox.showwarning(hd, "Nhập tháng/ngày âm lịch bạn cần xem rồi sau đó nhấn nút Xác nhận (nếu muốn xem ngày/tháng âm lịch có thể tham khảo thêm phần Âm lịch)")     
      def clicked1():
         hd1="- Ngày Hoàng đạo là: "; hd2="- Ngày Hắc đạo là: "
         if spin.get()=='1' or spin.get()=='7':
            mbox.showinfo(kq, hd1+"Tý, Sửu, Tỵ, Mùi\n"+hd2+"Ngọ, Măo, Hợi, Dậu")
         elif spin.get()=='2' or spin.get()=='8':
            mbox.showinfo(kq, hd1+"Dần, Măo, Dậu, Tý\n"+hd2+"Thân, Tỵ, Hợi, Sửu")
         elif spin.get()=='3' or spin.get()=='9':
            mbox.showinfo(kq, hd1+"Thìn, Tỵ, Dậu, Hợi\n"+hd2+"Tuất, Mùi, Măo, Sửu")
         elif spin.get()=='4' or spin.get()=='10':
            mbox.showinfo(kq, hd1+"Ngọ, Mùi, Hợi, Sửu\n"+hd2+"Tý, Dậu, Mẹo, Tỵ")
         elif spin.get()=='5' or spin.get()=='11':
            mbox.showinfo(kq, hd1+"Thân, Dậu, Sửu, Măo\n"+hd2+"Dần, Hợi, Mùi, Tỵ")
         elif spin.get()=='6' or spin.get()=='12':            
            mbox.showinfo(kq, hd1+"Tuất, Hợi, Măo, Tỵ\n"+hd2+"Thìn, Sửu, Mùi, Dậu")
         else:
            mbox.showerror("Lỗi",e)
      def clicked2():
         hd="Giờ hoàng đạo là: "; x = value.current()
         if x==0 or x==6:
            mbox.showinfo(kq, hd+"Tý, Sửu, Măo, Ngọ, Thân, Dậu")
         elif x==1 or x==7:
            mbox.showinfo(kq, hd+"Dần, Măo, Tỵ, Thân, Tuất, Hợi")
         elif x==2 or x==8:
            mbox.showinfo(kq, hd+"Tý, Sửu, Thìn, Tỵ, Mùi, Tuất")
         elif x==3 or x==9:
            mbox.showinfo(kq, hd+"Tý, Dần, Măo, Ngọ, Mùi, Dậu")
         elif x==4 or x==10:
            mbox.showinfo(kq, hd+"Dần, Thin, Tỵ, Thân, Dậu, Hợi")
         elif x==5 or x==11:
            mbox.showinfo(kq, hd+"Tý, Sửu, Thìn, Tỵ, Mùi, Tuất")
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel() 
      window.title("Hoàng đạo, hắc đạo"); window.geometry('500x100+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Ngày hoàng đạo, hắc đạo"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Giờ hoàng đạo"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Tháng âm lịch: "); lbl1.grid(column=0, row=0)
      lbl2 = Label(tab2, text="Ngày âm lịch:"); lbl2.grid(column=0, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=12, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=chi; value.grid(column=1, row=0)
      btn1 = Button(tab1, text="Xác nhận", command=clicked1); btn1.grid(column=2, row=0)
      btn2 = Button(tab2, text="Xác nhận", command=clicked2); btn2.grid(column=2, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def xayDung1(self):
      def info():
         mbox.showwarning(gt, "*Làm nhà là một việc hệ trọng nên cần phải tính toán xem xét thật kỹ lưỡng từng phần \
như sau:\n- Cửu trạch\n- Hạn cửu diệu (chi tiết xem phần Xem sao, xem hạn)\
\n- Hoang ốc\n- Kim lâu\n- Tam tai: là ba năm liên tiếp xảy ra bệnh tật, ốm đau, tai nạn, mất mát tài sản, tiền của, kiện tụng... \
Nếu như tuổi bạn năm nay rơi vào hạn tam tai thì không nên xây dựng và tu sửa nhà cửa \
(chi tiết xem phần Hung niên, tam tai)\n*Lưu ý: Độ tuổi làm nhà chỉ nên từ 18 đến 80 tuổi")
      def note():
         mbox.showwarning(ct, "Chữ in hoa là sao tốt, chữ in thường là sao xấu")
      def help():
         mbox.showwarning(hd, hda)
      def clicked():
         a=int(spin.get()); tx=['Bốn tốt: ','Ba tốt một xấu: ','Hai tốt hai xấu: ','Ba xấu một tốt: ']
         if a<18 or a>99:
            mbox.showwarning("Thông báo",e+"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 18 đến 99)")
         elif a in sao1:
            mbox.showinfo(kq, tx[1]+cuutrach[0]+' - '+cuudieu[0]+' - '+hoangoc[3]+' - '+kimlau[4])
         elif a in sao2:
            mbox.showinfo(kq, tx[3]+cuutrach[1]+' - '+cuudieu[1]+' - '+hoangoc[4]+' - '+kimlau[1])
         elif a==sao3[1] or a==sao3[2]:
            mbox.showinfo(kq, tx[3]+cuutrach[2]+' - '+cuudieu[2]+' - '+hoangoc[2]+' - '+kimlau[1])
         elif a in sao3!=sao3[0]!=sao3[1]!=sao3[2]:
            mbox.showinfo(kq, tx[2]+cuutrach[2]+' - '+cuudieu[2]+' - '+hoangoc[5]+' - '+kimlau[4])
         elif a==sao4[1] or a==sao4[2] or a==sao4[3]:
            mbox.showinfo(kq, tx[2]+cuutrach[3]+' - '+cuudieu[3]+' - '+hoangoc[3]+' - '+kimlau[4])
         elif a in sao4 and a!=sao4[0]!=sao4[1]!=sao4[2]!=sao4[3]:
            mbox.showinfo(kq, tx[3]+cuutrach[3]+' - '+cuudieu[3]+' - '+hoangoc[0]+' - '+kimlau[2])
         elif a==sao5[1] or a==sao5[2] or a==sao5[3] or a==sao5[4]:
            mbox.showinfo(kq, tx[2]+cuutrach[4]+' - '+cuudieu[4]+' - '+hoangoc[3]+' - '+kimlau[2])
         elif a==sao5[5] or a==sao5[6] or a==sao5[7] or a==sao5[8]:
            mbox.showinfo(kq, tx[1]+cuutrach[4]+' - '+cuudieu[4]+' - '+hoangoc[1]+' - '+kimlau[4])
         elif a in sao6 and a!=sao4[6]!=sao4[7]!=sao4[8]:
            mbox.showinfo(kq, tx[2]+cuutrach[5]+' - '+cuudieu[5]+' - '+hoangoc[5]+' - '+kimlau[4])
         elif a==sao6[6] or a==sao4[7] or a==sao4[8]:
            mbox.showinfo(kq, tx[4]+cuutrach[5]+' - '+cuudieu[5]+' - '+hoangoc[2]+' - '+kimlau[3])
         elif a in sao7 and a!=sao7[0]!=sao7[8]!=sao7[9]:
            mbox.showinfo(kq, tx[3]+cuutrach[6]+' - '+cuudieu[6]+' - '+hoangoc[0]+' - '+kimlau[3])
         elif a in sao8 and a!=sao8[0]!=sao8[8]!=sao8[9]:
            mbox.showinfo(kq, tx[0]+cuutrach[7]+' - '+cuudieu[7]+' - '+hoangoc[1]+' - '+kimlau[4])
         elif a in sao9:
            mbox.showinfo(kq, tx[2]+cuutrach[8]+' - '+cuudieu[8]+' - '+hoangoc[2]+' - '+kimlau[0])
      info()
      window = Toplevel() 
      window.title("Xem tuổi xây nhà"); window.geometry('400x50+200+200')
      lbl=Label(window, text="Tuổi xây nhà của bạn: "); lbl.grid(column=0, row=0)
      spin = Spinbox(window, fg="blue", font=12, from_=18, to=99, width=10); spin.grid(column=1,row=0)
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=2, row=0)
      menuBar = Menu(window)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=ct, command=note); menuBar.add_command(label=hd, command=help) 
      window.config(menu=menuBar)
      window.mainloop()      
   def xayDung2(self):
      def info():
         mbox.showwarning(gt, "- Trong xây dựng, tu tạo nhà cửa ngoài những điều cần tránh, hướng nhà cũng rất quan trọng. Nếu tránh được những điều xấu như đã nêu \
ở phần Xây dựng nhà cửa mà hướng nhà vào hướng xấu so với tuổi của chủ nhà thì cũng rất nguy hiểm\n- Lưu ý: Độ tuổi làm nhà chỉ nên từ 18-80 tuổi")
      def help():
         mbox.showwarning(hd, hdas)
      ht = "- Hướng tốt (xếp theo thứ tự giảm dần): "; hx = "- Hướng xấu nhất (có thể nguy hiểm đến tính mạng): "; hk = "- Còn lại các hướng khác đều xấu"
      def clicked1():
         a = value.current(); s=var.get()
         if a<0 or a>59 or s<0 or s>1:
            mbox.showerror("Lỗi",e)
         elif (a==7 and s==1) or (a==51 and s==1) or (a==22 and s==1) or (a==23 and s==1) or (a==38 and s==1) or (a==53 and s==1)\
              or (a==8 and s==0) or (a==37 and s==0) or (a==52 and s==0):
            mbox.showinfo(kq, ht+"\n + "+huong[6]+"\n + "+huong[7]+"\n + "+huong[0]+"\n + "+huong[2]+"\n"+hx+"\n + "+huong[1]+"\n"+hk)
         elif (a==s==1) or (a==16 and s==1) or (a==3 and s==1) or (a==32 and s==1) or (a==47 and s==1) or (a==18 and s==1)\
              or (a==40 and s==0) or (a==28 and s==0) or (a==47 and s==0) or (a==14 and s==0) or (a==29 and s==0) or (a==25 and s==0) or (a==59 and s==0):
            mbox.showinfo(kq, ht+"\n + "+huong[2]+"\n + "+huong[0]+"\n + "+huong[7]+"\n + "+huong[6]+"\n"+hx+"\n + "+huong[4]+"\n"+hk)
         elif (a==11 and s==1) or (a==55 and s==1) or (a==26 and s==1) or (a==56 and s==1) or (a==42 and s==1) or (a==57 and s==1) or (a==28 and s==1)\
              or (a==13 and s==1) or (a==14 and s==1) or (a==29 and s==1) or (a==25 and s==1) or (a==59 and s==1)\
              or (a==16 and s==0) or (a==32 and s==0) or (a==3 and s==0) or (a==18 and s==0):
            mbox.showinfo(kq, ht+"\n + "+huong[4]+"\n + "+huong[5]+"\n + "+huong[3]+"\n + "+huong[1]+"\n"+hx+"\n + "+huong[2]+"\n"+hk)
         elif (a==37 and s==1) or (a==52 and s==1) or (a==8 and s==1) or (a==7 and s==0) or (a==51 and s==0) or (a==22 and s==0) or (a==23 and s==0)\
              or (a==9 and s==0) or (a==38 and s==0) or (a==53 and s==0):
            mbox.showinfo(kq, ht+"\n + "+huong[5]+"\n + "+huong[4]+"\n + "+huong[1]+"\n + "+huong[3]+"\n"+hx+"\n + "+huong[0]+"\n"+hk)
         elif (a==2 and s==1) or (a==46 and s==1) or (a==17 and s==1) or (a==33 and s==1) or (a==4 and s==1) or (a==48 and s==1) or (a==23 and s==1)\
              or (a==12 and s==0) or (a==41 and s==0) or (a==27 and s==0) or (a==57 and s==0) or (a==44 and s==0) or (a==48 and s==0)\
              or (a==43 and s==0) or (a==58 and s==0) or (a==10 and s==0):
            mbox.showinfo(kq, ht+"\n + "+huong[1]+"\n + "+huong[3]+"\n + "+huong[5]+"\n + "+huong[4]+"\n"+hx+"\n + "+huong[6]+"\n"+hk)
         elif (a==31 and s==1) or (a==59 and s==1) or (a==19 and s==1) or (a==34 and s==1) or (a==0 and s==1) or (a==49 and s==1) or (a==15 and s==1)\
              or (a==30 and s==1) or (a==11 and s==0) or (a==55 and s==0) or (a==26 and s==0) or (a==56 and s==0) or (a==42 and s==0) or (a==28 and s==0):
            mbox.showinfo(kq, ht+"\n + "+huong[7]+"\n + "+huong[6]+"\n + "+huong[2]+"\n + "+huong[0]+"\n"+hx+"\n + "+huong[3]+"\n"+hk)
         elif a==6 or a==50 or a==21 or a==36 or a==24 or a==39 or a==5 or a==54 or a==20 or a==35:
            mbox.showinfo(kq, ht+"\n + "+huong[0]+"\n + "+huong[2]+"\n + "+huong[6]+"\n + "+huong[7]+"\n"+hx+"\n + "+huong[5]+"\n"+hk)
         else:
            mbox.showinfo(kq, ht+"\n + "+huong[3]+"\n + "+huong[1]+"\n + "+huong[4]+"\n + "+huong[5]+"\n"+hx+"\n + "+huong[7]+"\n"+hk)
      def clicked2():
         a = int(spin.get()); s = var.get(); r=a%60
         if (r in huong1m and s==2) or (r in huong1f and s==3):
            mbox.showinfo(kq, ht+"\n + "+huong[2]+"\n + "+huong[0]+"\n + "+huong[7]+"\n + "+huong[6]+"\n"+hx+"\n + "+huong[4]+"\n"+hk)
         elif (r in huong2m and s==2) or (r in huong2f and s==3):
            mbox.showinfo(kq, ht+"\n + "+huong[4]+"\n + "+huong[5]+"\n + "+huong[3]+"\n + "+huong[1]+"\n"+hx+"\n + "+huong[2]+"\n"+hk)
         elif (r in huong3 and s==2) or (r in huong4 and s==3):
            mbox.showinfo(kq, ht+"\n + "+huong[5]+"\n + "+huong[4]+"\n + "+huong[1]+"\n + "+huong[3]+"\n"+hx+"\n + "+huong[0]+"\n"+hk)
         elif (r in huong5m and s==2) or (r in huong5f and s==3):
            mbox.showinfo(kq, ht+"\n + "+huong[3]+"\n + "+huong[1]+"\n + "+huong[4]+"\n + "+huong[5]+"\n"+hx+"\n + "+huong[7]+"\n"+hk)
         elif (r in huong6m and s==2) or (r in huong6f and s==3):
            mbox.showinfo(kq, ht+"\n + "+huong[1]+"\n + "+huong[3]+"\n + "+huong[5]+"\n + "+huong[4]+"\n"+hx+"\n + "+huong[6]+"\n"+hk)
         elif (r in huong7m and s==2) or (r in huong7f and s==3):
            mbox.showinfo(kq, ht+"\n + "+huong[7]+"\n + "+huong[6]+"\n + "+huong[2]+"\n + "+huong[0]+"\n"+hx+"\n + "+huong[3]+"\n"+hk)
         elif (r in huong4 and s==2) or (r in huong3 and s==3):
            mbox.showinfo(kq, ht+"\n + "+huong[6]+"\n + "+huong[7]+"\n + "+huong[0]+"\n + "+huong[2]+"\n"+hx+"\n + "+huong[1]+"\n"+hk)
         elif r in huong8:
            mbox.showinfo(kq, ht+"\n + "+huong[0]+"\n + "+huong[2]+"\n + "+huong[6]+"\n + "+huong[7]+"\n"+hx+"\n + "+huong[5]+"\n"+hk)
         else:
            mbox.showerror("Lỗi",e)
      info()
      window = Toplevel(); var = IntVar()
      window.title("Hướng nhà"); window.geometry('700x50+100+200')
      tab_control = ttk.Notebook(window); tab1 = ttk.Frame(tab_control); tab2 = ttk.Frame(tab_control)
      tab_control.add(tab1, text="Tra bằng năm sinh dương lịch"); tab_control.pack(expand=1, fill='both')
      tab_control.add(tab2, text="Tra bằng năm sinh âm lịch"); tab_control.pack(expand=1, fill='both')
      lbl1 = Label(tab1, text="Năm sinh dương lịch: "); lbl2 = Label(tab2, text="Năm sinh âm lịch: ")
      lbl3 = Label(tab1, text="Giới tính của bạn: "); lbl4 = Label(tab2, text="Giới tính của bạn: ")
      lbl1.grid(column=0, row=0); lbl2.grid(column=0, row=0); lbl3.grid(column=2, row=0); lbl4.grid(column=2, row=0)
      spin = Spinbox(tab1, fg="blue", font=12, from_=1, to=9999, width=14); spin.grid(column=1,row=0)
      value = Combobox(tab2); value['values']=canchi; value.grid(column=1, row=0)
      rad1 = Radiobutton(tab2, text='Nam', value=1, variable=var); rad1.grid(column=3, row=0)
      rad0 = Radiobutton(tab2, text='Nữ', value=0, variable=var); rad0.grid(column=4, row=0)
      rad2 = Radiobutton(tab1, text='Nam', value=2, variable=var); rad2.grid(column=3, row=0)
      rad3 = Radiobutton(tab1, text='Nữ', value=3, variable=var); rad3.grid(column=4, row=0)      
      btn1 = Button(tab1, text="Xác nhận", command=clicked2); btn2 = Button(tab2, text="Xác nhận", command=clicked1) 
      btn1.grid(column=5, row=0); btn2.grid(column=5, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def hoangDao1(self):
      def info():
         mbox.showwarning(gt, "Trong chiêm tinh học và thiên văn học thời cổ, các cung Hoàng Đạo là một vòng tròn 360o và được phân chia làm 12 nhánh, mỗi nhánh \
tương ứng với một cung, góc 30o. Cung Hoàng Đạo tạo ra bởi các nhà chiêm tinh học Babylon cổ đại từ những năm 1645 trước Công nguyên. Vòng tròn 12 cung Hoàng Đạo \
hoàn hảo với 12 cung tương xứng với bốn mùa và 12 tháng. Các cung được phân chia làm bốn nhóm yếu tố (Lửa, Nước, Khí, Đất), mỗi nhóm yếu tố gồm 3 cung đại diện cho \
các cung có tính cách tương đồng với nhau. Theo các nhà thiên văn học thời cổ đại, trong khoảng thời gian chừng 30 - 31 ngày, Mặt Trời sẽ đi qua một trong mười hai \
chòm sao đặc biệt. Ai sinh ra trong thời gian Mặt Trời đi qua chòm sao nào thì họ sẽ được chòm sao đó chiếu mệnh và tính cách của họ cũng bị chòm sao ảnh hưởng \
nhiều. 12 chòm sao tạo thành 12 cung trong vòng tròn Hoàng đạo, có nghĩa: Đường đi của mặt trời. Theo phương Tây, vòng tròn này tên là Horoscope. Tiếng Hy Lạp là \
Zodiakus Kyklos (ζωδιακός κύκλος):\"Vòng tròn của các động vật.\"")
      def help():
         mbox.showwarning(hd, hddl2)
      def clicked():
         d = int(spin1.get()); m = int(spin2.get()); y = int(spin3.get())
         if (d==31 and m==4) or (d==31 and m==6) or (d==31 and m==9) or (d==31 and m==11) or (d==31 and m==2) or (d==30 and m==2) or (d==29 and m==2 and y%4!=0)\
            or d<1 or d>31 or m<1 or m>12 or y<1:
            mbox.showerror("Lỗi",e)
         else: 
               if (m==3 and d>20 and d<32) or (m==4 and d<20):
                  mbox.showinfo(kq, "Cung: Bạch Dương")
               elif (m==4 and d>19 and d<31) or (m==5 and d<21):
                  mbox.showinfo(kq, "Cung: Kim Ngưu")
               elif (m==5 and d>20 and d<32) or (m==6 and d<22):
                  mbox.showinfo(kq, "Cung: Song Tử")
               elif (m==6 and d>21 and d<31) or (m==7 and d<23):
                  mbox.showinfo(kq, "Cung: Cự Giải")
               elif (m==7 and d>22 and d<32) or (m==8 and d<23):
                  mbox.showinfo(kq, "Cung: Sư Tử")
               elif (m==8 and d>22 and d<32) or (m==9 and d<23):
                  mbox.showinfo(kq, "Cung: Xử Nữ")
               elif (m==9 and d>22 and d<31) or (m==10 and d<23):
                  mbox.showinfo(kq, "Cung: Thiên Bình")
               elif (m==10 and d>22 and d<32) or (m==11 and d<23):
                  mbox.showinfo(kq, "Cung: Thiên Yết/Thần Nông")
               elif (m==11 and d>22 and d<31) or (m==12 and d<22):
                  mbox.showinfo(kq, "Cung: Nhân Mã")
               elif (m==12 and d>21 and d<32) or (m==1 and d<20):
                  mbox.showinfo(kq, "Cung: Ma Kết")
               elif (m==1 and d>19 and d<32) or (m==2 and d<19):
                  mbox.showinfo(kq, "Cung: Bảo Bình")
               else:
                  mbox.showinfo(kq, "Cung: Song Ngư")
      def list():
         mbox.showinfo(ds, "- Bạch Dương: 21/3 - 19/4\n- Kim Ngưu: 20/4 - 20/5\n- Song Tử: 21/5 - 21/6\n- Cự Giải: 22/6 - 22/7\n- Sư Tử: 23/7 - 22/8\n- Xử Nữ: 23/8 \
- 22/9\n- Thiên Bình: 23/9 - 22/10\n- Thiên Yết/Thần Nông: 23/10 - 22/11\n- Nhân Mã: 23/11 - 21/12\n- Ma Kết: 22/12 - 19/1\n- Bảo Bình: 20/1 - 18/2\n- Song Ngư: \
19/1 - 20/2")
      info()
      window = Toplevel()
      window.title("Tra cung Hoàng đạo"); window.geometry('700x50+100+200')
      lbl = Label(window, text="Ngày tháng năm sinh: "); lbl.grid(column=0, row=0)
      spin1 = Spinbox(window, fg="blue", font=12, from_=1, to=31, width=14); spin1.grid(column=1,row=0)
      spin2 = Spinbox(window, fg="blue", font=12, from_=1, to=12, width=14); spin2.grid(column=2,row=0)
      spin3 = Spinbox(window, fg="blue", font=12, from_=1, to=9999, width=14); spin3.grid(column=3,row=0)
      btn1 = Button(window, text="Xác nhận", command=clicked); btn1.grid(column=4, row=0)
      menuBar = Menu(window); window.config(menu=menuBar)
      menuBar.add_command(label=gt, command=info); menuBar.add_command(label=ds, command=list); menuBar.add_command(label=hd, command=help)       
      window.mainloop()
   def onWidget(self):
      mbox.showerror("Lỗi",e)
   def onWarn(self):
      mbox.showwarning("Thông báo", "Tính năng sắp ra mắt!\nXin vui lòng trở lại sau.")
   def onQuit(self):
      mbox.askquestion("Xác nhận", "Bạn chắc chắn muốn thoát không?")
   def onGame(self):
      mbox.showinfo("Thông tin", "Xin chúc mừng")
window = Tk()
ex = boi(window)
window.geometry("450x400+850+100")
window.mainloop()
