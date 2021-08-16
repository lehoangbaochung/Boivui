from tkinter.ttk import Frame, Button
from tkinter.ttk import *
from tkinter import * 
from tkinter import Tk, Canvas, BOTH, W, Menu, ttk, Label, scrolledtext, BOTH, SUNKEN, filedialog
from tkinter.colorchooser import askcolor
from turtle import *
import tkinter.messagebox as mbox
import tkinter as tk
import math
#định nghĩa
canchi=['Giáp Tý','Bính Tý','Mậu Tý','Canh Tý','Nhâm Tý','Ất Sửu','Đinh Sửu','Kỷ Sửu','Tân Sửu','Quý Sửu','Bính Dần','Mậu Dần','Canh Dần','Nhâm Dần','Giáp Dần',
'Đinh Măo','Kỷ Măo','Tân Măo','Quý Măo','Ất Măo','Mậu Thìn','Canh Thìn','Nhâm Thìn','Giáp Thìn','Bính Thìn','Kỷ Tỵ','Tân Tỵ','Quý Tỵ','Ất Tỵ','Đinh Tỵ','Canh Ngọ',
'Nhâm Ngọ','Giáp Ngọ','Bính Ngọ','Mậu Ngọ','Tân Mùi','Quý Mùi','Ất Mùi','Đinh Mùi','Kỷ Mùi','Nhâm Thân','Giáp Thân','Bính Thân','Canh Thân','Mậu Thân','Quý Dậu',
'Ất Dậu','Đinh Dậu','Kỷ Dậu','Tân Dậu','Giáp Tuất','Bính Tuất','Mậu Tuất','Canh Tuất','Nhâm Tuất','Ất Hợi','Đinh Hợi','Kỷ Hợi','Tân Hợi','Quý Hợi']
can=['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý']
can0=['Quý','Quy','quy','quý','qui','quí','Quí','Qui','QUÍ','QUÝ','QUI','QUY']; can1=['Giáp','Giap','giap','giáp','GIÁP','GIAP']
can2=['Ất','At','at','ất','ẤT','AT']; can3=['Bính','Binh','binh','bính','BÍNH','BINH']
can4=['Đinh','Dinh','đinh','dinh','ĐINH','DINH']; can5=['Mậu','Mau','mau','mậu','MẬU','MAU']
can6=['Kỷ','Ky','ky','kỷ','kỉ','ki','Kỉ','Ki','KỶ','KỈ','KY','KI']; can7=['Canh','canh','CANH']
can8=['Tân','Tan','tan','tân','TÂN','TAN']; can9=['Nhâm','Nham','nham','nhâm','NHÂM','NHAM']
chi=['Tý','Sửu','Dần','Măo','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']
chi0=['Hợi','Hoi','hoi','hợi','HỢI','HOI']; chi1=['Tý','tí','tý','ti','Ti','Tí','TÝ','TÍ','TI']
chi2=['Sửu','Suu','suu','sửu','SỬU','SUU']; chi3=['Dần','Dan','dan','dần','DẦN','DAN']
chi4=['Măo','Mao','mao','măo','Mẹo','Meo','meo','mẹo','MĂO','MẸO','MAO','MEO']; chi5=['Thìn','Thin','thin','thìn','THÌN','THIN']
chi6=['Tỵ','Ty','ty','tỵ','TỴ','TY']; chi7=['Ngọ','Ngo','ngo','ngọ','NGỌ','NGO']
chi8=['Mùi','Mui','mui','mùi','MÙI','MUI']; chi9=['Thân','Than','than','thân','THÂN','THAN']
chi10=['Dậu','Dau','dau','dậu','DẬU','DAU']; chi11=['Tuất','Tuat','tuat','tuất','TUẤT','TUAT']
bq=['Càn','Khảm','Cấn','Chấn','Tốn','Ly','Khôn','Đoài']
bq1=['Càn','càn','CÀN']; bq2=['Khảm','Kham','kham','khảm','KHẢM','KHAM']
bq3=['Cấn','cấn','CẤN']; bq4=['Chấn','Chan','chan','chấn','CHẤN','CHAN']
bq5=['Tốn','Ton','ton','tốn','TỐN','TON']; bq6=['Ly','ly','li','Li','LY','LI']
bq7=['Khôn','Khon','khon','khôn','KHÔN','KHON']; bq8=['Đoài','Doai','doai','đoài','ĐOÀI','DOAI']
nh=['Kim','Mộc','Thuỷ','Hoả','Thổ']
nh1=['Kim','kim','KIM']; nh2=['Mộc','Moc','moc','mộc','MỘC','MOC']; nh3=['Thuỷ','Thuy','thuy','thuỷ','THUỶ','THUY']
nh4=['Hoả','Hoa','hoa','hoả','HOẢ','HOA']; nh5=['Thổ','Tho','tho','thổ','THỔ','THO']
bqhh=['Sinh khí','Phước đức','Thiên y','Phục vị','Tuyệt mệnh','Hoạ hại','Ngũ quỷ','Lục sát']
bqhh1=['Sinh khí','Sinh khi','sinh khí','sinh khi','SINH KHÍ','SINH KHI']; bqhh2=['Phước đức','Phuoc duc','phước đức','phuoc duc','PHƯỚC ĐỨC','PHUOC DUC']
bqhh3=['Thiên y','Thien y','thiên y','thien y','THIÊN Y','THIEN Y']; bqhh4=['Phục vị','Phuc vi','phục vị','phuc vi','PHỤC VỊ','PHUC VI']
bqhh5=['Tuyệt mệnh','Tuyet menh','tuyệt mệnh','tuyet menh','TUYỆT MỆNH','TUYET MENH']; bqhh6=['Hoạ hại','Hoa hai','hoạ hại','hoa hai','HOẠ HẠI','HOA HAI']
bqhh7=['Ngũ quỷ','Ngu quy','Ngũ quỉ','Ngu qui','ngũ quỷ','ngũ quỉ','ngu quy','ngu qui','NGŨ QUỶ','NGŨ QUỈ','NGU QUY','NGU QUI']
bqhh8=['Lục sát','Luc sat','lục sát','luc sat','LỤC SÁT','LUC SAT']
cuutrach=['TRẠCH PHÚC', 'TRẠCH ĐỨC', 'Trạch bại', 'Trạch hư', 'Trạch khốc', 'Trạch quỷ', 'Trạch tử', 'TRẠCH BẢO', 'TRẠCH LỘC']
hoangoc=['CUNG CÁT', 'CUNG NGHI', 'Địa Sát', 'TẤN TÀI', 'Thụ Tử', 'Hoang Ốc']
kimlau=['Kim Lâu thân', 'Kim Lâu thê', 'Kim Lâu tử', 'Kim Lâu súc','KHÔNG PHẠM KIM LÂU']
cuudieu=['La Hán', 'Thổ Tú', 'THUỶ DIỆU', 'Thái Bạch', 'THÁI DƯƠNG', 'Vân Hán', 'Kế Đô', 'THÁI ÂM', 'MỘC ĐỨC']
ngude=['Thanh Đế','Huỳnh Đế','Bạch Đế','Hắc Đế','Xích Đế']; huong=['Đông','Tây','Đông Nam','Đông Bắc','Tây Nam','Tây Bắc','Nam','Bắc']
sao1=[10,19,28,37,46,55,64,73,82,91]; sao2=[11,20,29,38,47,56,65,74,83,92]; sao3=[12,21,30,39,48,57,66,75,84,93]; sao4=[13,22,31,40,49,58,67,76,85,94]
sao5=[14,23,32,41,50,59,68,77,86,95]; sao6=[15,24,33,42,51,60,69,78,87,96]; sao7=[16,25,34,43,52,61,70,79,88,97]; sao8=[17,26,35,44,53,62,71,80,89,98]
sao9=[18,27,36,45,54,63,72,81,90,99]; han1=[11,19,20,28,37,46,55,64,73,82,91,99]; han2=[12,21,29,30,38,47,56,65,74,83,92]; han3=[13,22,31,39,40,48,57,66,75,84,93]
han4=[14,23,32,41,49,50,58,67,76,85,94]; han5=[15,24,33,42,51,59,60,68,77,86,95]; han6=[16,25,34,43,52,61,69,70,78,87,96]; han7=[17,26,35,44,53,62,71,79,80,88,97]
han8=[10,18,27,36,45,54,63,72,81,89,90,98]
huong1m=[16,19,34,37,40,43]; huong1f=[3,12,37,45,54,57]; huong2m=[3,9,15,18,21,27,36,39,42,45,54,57]; huong2f=[19,34,40,43]; huong3=[35,38,41]
huong4=[26,29,32,44,47,50,53]; huong5m=[0,6,24,30,33,48,51]; huong5f=[1,4,7,10,22,25,28,31,46,52,55,58]; huong6m=[25,28,31,46,49,52]; huong6f=[24,30,33,39,48,49,51]
huong7m=[1,4,7,10,13,22,55,58]; huong7f=[15,18,21,27,36,42]; huong8=[2,5,8,11,14,17,20,23,56,59]
ngonngu=['Tiếng Việt','English','中文简体']
ad="- Âm dương:"; nh="- Ngũ hành:"; kq="Kết quả"
e="Lỗi nhập dữ liệu.\nVui lòng nhập lại!"
f="Đă xảy ra lỗi trong quá trình nhập dữ liệu!"
iny="*Nhập năm sinh của bạn: "; ina="*Nhập tuổi của bạn: "; ins="*Lựa chọn giới tính của bạn (nam nhấn Enter, nữ nhấn Space và Enter):"
#main
class boi(Frame):
   def __init__(self, parent):
      Frame.__init__(self, parent)  
      self.parent = parent 
      self.initUI()      
   def initUI(self):
      self.parent.title("Bói vui 2019")
      menuBar = Menu(self.parent)
      #chọn màu nền
      self.frame = Frame(self, border=1, relief=SUNKEN, width=450, height=400)
      self.frame.place(x=0, y=0)
      #nút phải chuột
      self.menu = Menu(self.parent, tearoff=0)
      self.menu.add_command(label="Làm mới", command=self.bell())
      self.menu.add_command(label="Giới thiệu", command=self.bell())
      self.menu.add_command(label="Thoát", command=self.master.destroy) 
      self.parent.bind("<Button-3>", self.rightKey)
      #định nghĩa menu chính
      self.parent.config(menu=menuBar)
      fileMenu1 = Menu(menuBar); fileMenu2 = Menu(menuBar); fileMenu3 = Menu(menuBar)
      fileMenu11 = Menu(menuBar); fileMenu12 = Menu(menuBar); fileMenu13 = Menu(menuBar); fileMenu14 = Menu(menuBar); fileMenu15 = Menu(menuBar)
      fileMenu16 = Menu(menuBar)
      #các menu có nhánh
      submenu1 = Menu(fileMenu1); submenu2 = Menu(fileMenu1); submenu3 = Menu(fileMenu1); submenu4 = Menu(fileMenu1); 
      submenu6 = Menu(fileMenu1); submenu7 = Menu(fileMenu1); submenu8 = Menu(fileMenu1); submenu9 = Menu(fileMenu1); submenu10 = Menu(fileMenu1)
      submenu11 = Menu(fileMenu1); submenu12 = Menu(fileMenu1); submenu13 = Menu(fileMenu1); submenu14 = Menu(fileMenu1); submenu15= Menu(fileMenu1)
      submenu21 = Menu(fileMenu2); submenu22 = Menu(fileMenu2);
      submenu31 = Menu(fileMenu3);
      #menu nhánh (1)
      fileMenu1.add_cascade(label="Hôn nhân", menu=submenu1); fileMenu1.add_cascade(label="Ngũ hành", menu=submenu2)
      fileMenu1.add_cascade(label="Bát quái", menu=submenu3); fileMenu1.add_command(label="Thiên can", command=self.thienCan)
      fileMenu1.add_cascade(label="Địa chi (con giáp)", menu=submenu4); fileMenu1.add_cascade(label="Dương lịch", menu=submenu6)
      fileMenu1.add_command(label="Âm lịch", command=self.amLich); fileMenu1.add_cascade(label="Ngũ đế", menu=submenu8)
      fileMenu1.add_cascade(label="Ngày tốt, ngày xấu", menu=submenu9); fileMenu1.add_cascade(label="Xem sao, xem hạn", menu=submenu10)
      fileMenu1.add_command(label="Hung niên - tam tai", command=self.hungTai); fileMenu1.add_cascade(label="Vận mệnh con người qua năm sinh", menu=submenu12)
      fileMenu1.add_cascade(label="Ngày hoàng đạo, ngày hắc đạo", menu=submenu13)
      fileMenu1.add_cascade(label="Xây dựng nhà cửa, xuất hành", menu=submenu14)
      fileMenu1.add_cascade(label="Khai trương, xông nhà", menu=submenu15)
      submenu22.add_command(label="Nhạc nền", command=self)
      submenu22.add_command(label="Nhạc thông báo    ✓", command=self)
      #menu con cấp 2 (1)
      submenu1.add_cascade(label="Bát quái", menu=fileMenu11); submenu1.add_command(label="Ngũ hành"); submenu1.add_command(label="Ngũ đế", command=self)                                                                                                                            
      submenu1.add_command(label="Thiên can hợp hôn", command=self.honNhan4); submenu1.add_command(label="Địa chi hợp hôn", command=self.honNhan5)
      submenu1.add_command(label="Tự kiểm tra việc hôn nhân", command=self.honNhan6); submenu1.add_cascade(label="Chọn ngày tháng tốt cho hôn nhân", menu=fileMenu12)
      submenu2.add_cascade(label="Tra ngũ hành", menu=fileMenu13); submenu2.add_command(label="Sơ đồ ngũ hành", command=self)
      submenu2.add_command(label="Các nguyên tắc ngũ hành", command=self.nguHanh3)
      submenu3.add_cascade(label="Tra bát quái", menu=fileMenu14)
      submenu4.add_command(label="Địa chi (con giáp)", command=self.diaChi1); submenu4.add_command(label="Sự tương quan giữa 12 địa chi (con giáp)", command=self)
      submenu6.add_command(label="Tra thứ tự ngày, tuần trong năm", command=self.duongLich1)
      submenu6.add_command(label="Tra thứ trong tuần", command=self.duongLich2)
      submenu8.add_cascade(label="Tra ngũ đế", menu=fileMenu15)
      submenu10.add_command(label="Tra sao, tra hạn", command=self.saoHan1); submenu10.add_command(label="Cách tiễn sao xấu và nghênh sao tốt", command=self.saoHan2)
      submenu10.add_command(label="Cửu diệu tinh (sơ đồ bày đèn cúng sao)", command=self.saoHan3)
      submenu12.add_command(label="Xem màu sắc và số may mắn", command=self.vanMenh1)
      submenu13.add_command(label="Xem ngày hoàng đạo, ngày hắc đạo", command=self.hoangHac1)
      submenu13.add_command(label="Xem giờ hoàng đạo", command=self.hoangHac2)
      submenu14.add_command(label="Xem tuổi xây nhà", command=self.xayDung1)
      submenu14.add_command(label="Hướng nhà", command=self.xayDung2)
      #menu con cấp 3 (1)
      fileMenu11.add_command(label="Bát quái hợp hôn", command=self.honNhan1); fileMenu11.add_command(label="Bát san giao chiến", command=self.honNhan2)
      fileMenu11.add_command(label="Bát san tuyệt mệnh", command=self.honNhan3);
      fileMenu12.add_command(label="Chọn ngày tốt", command=self.honNhan7)
      fileMenu12.add_command(label="Chọn tháng tốt", command=self.honNhan8)
      fileMenu13.add_command(label="Theo năm dương lịch", command=self.nguHanh1); fileMenu13.add_command(label="Theo năm can chi", command=self)
      fileMenu14.add_command(label="Theo năm dương lịch", command=self.batQuai1); fileMenu14.add_command(label="Theo năm can chi", command=self.batQuai2)
      fileMenu15.add_command(label="Theo năm dương lịch", command=self.nguDe1); fileMenu15.add_command(label="Theo năm can chi", command=self)
      #cài đặt (2)
      fileMenu2.add_cascade(label="Ngôn ngữ", menu=submenu21)
      fileMenu2.add_cascade(label="Âm thanh", menu=submenu22)
      fileMenu2.add_cascade(label="Màu nền", command=self.chooseColor)
      fileMenu2.add_command(label="Thoát", command=self.master.destroy)
      #thông tin (3)
      fileMenu3.add_command(label="Giới thiệu", command=self.introduce)
      fileMenu3.add_command(label="Kiểm tra cập nhật", command=self.update)
      #thanh công cụ mẹ (1-2-3)
      menuBar.add_cascade(label="Menu", menu=fileMenu1)
      menuBar.add_command(label="Cài đặt", command=self.settings)
      menuBar.add_cascade(label="Thông tin", menu=fileMenu3)
      #widgets
      c1 = Button(self, text="Hôn nhân", command=self.honNhan7)
      c1.grid(row=0, column=0, padx=5, pady=5)
      c2 = Button(self, text="Ngũ hành", command=self.nguHanh1)
      c2.grid(row=1, column=0, padx=5, pady=5)
      c3 = Button(self, text="Bát quái", command=self.batQuai1)
      c3.grid(row=2, column=0, padx=5, pady=5)
      c4 = Button(self, text="Thiên can", command=self.thienCan)
      c4.grid(row=3, column=0, padx=5, pady=5)
      c5 = Button(self, text="Địa chi", command=self.diaChi1)
      c5.grid(row=4, column=0, padx=5, pady=5)
      c6 = Button(self, text="Dương lịch", command=self.duongLich1)
      c6.grid(row=5, column=0, padx=5, pady=5)
      c7 = Button(self, text="Âm lịch", command=self.amLich)
      c7.grid(row=6, column=0, padx=5, pady=5)
      c8 = Button(self, text="Ngũ đế".center(50,' '), command=self.onWarn)
      c8.grid(row=0, column=1, padx=5, pady=5)
      c9 = Button(self, text="Sao tốt, sao xấu".center(45,' '), command=self.onWarn)
      c9.grid(row=1, column=1, padx=5, pady=5)
      c10 = Button(self, text="Xem sao, xem hạn".center(41,' '), command=self.saoHan1)
      c10.grid(row=2, column=1, padx=5, pady=5)
      c11 = Button(self, text="Hung niên, tam tai".center(42,' '), command=self.hungTai)
      c11.grid(row=3, column=1, padx=5, pady=5)
      c12 = Button(self, text="Sự tương quan giữa 12 con giáp ", command=self.onWarn)
      c12.grid(row=4, column=1, padx=5, pady=5)
      c13 = Button(self, text=" Ngày hoàng đạo, ngày hắc đạo ", command=self.hoangHac1)
      c13.grid(row=5, column=1, padx=5, pady=5)
      c14 = Button(self, text="   Và nhiều tính năng hơn nữa...   ", command=self.onWarn)
      c14.grid(row=6, column=1, padx=5, pady=5)
      self.pack(fill=BOTH, expand=1)
      self.pack()
   def settings(self):
      from tkinter import messagebox
      window = Tk() 
      window.title("Cài đặt") 
      window.geometry('400x300+200+200')
      lbl = Label(window, text="*Ngôn ngữ:"); lbl.grid(column=0, row=0)
      gt = Combobox(window) 
      gt['values']=ngonngu
      gt.current(0)
      gt.grid(column=1, row=0)
      lbl = Label(window, text=""); lbl.grid(column=0, row=1)
      lbl = Label(window, text="*Âm thanh:"); lbl.grid(column=0, row=2)
      chk1_state = BooleanVar(); chk2_state = BooleanVar()
      chk1 = Checkbutton(window, text='Nền', var=chk1_state); chk1.grid(column=2, row=2)
      chk2 = Checkbutton(window, text='Thông báo', var=chk2_state); chk2.grid(column=1, row=2)
      lbl = Label(window, text=""); lbl.grid(column=0, row=3)
      lbl = Label(window, text="*Ảnh nền:"); lbl.grid(column=0, row=4)
      def browse():
         file = filedialog.askopenfilename(filetypes = (("Image files","*.jpg,*.png"),("All files","*.*")))
      btn = Button(window, text="Duyệt tập tin...", command=browse) 
      btn.grid(column=1, row=4)      
      window.mainloop()
   def chooseColor(self):
      (rgb, hx) = askcolor()
      self.frame.config(bg=hx)
   def rightKey(self, e):
        self.menu.post(e.x_root, e.y_root)
   def introduce(self):
      print("*Giới thiệu về ứng dụng:\n- Phiên bản: 2.0\n- Tác giả: Bảo Chung (#ZH)\n- Ngày phát hành: 29/6/2019\n- Email: dragonelf282@gmail.com")
      print("- FB: Chung Chung\n- Youtube: Chung Chung")
      print("-"*50)
   def update(self):
      print("*Cập nhật phần mềm:\n- Đang kiểm tra cập nhật...")
      print("|"*70,"100%")
      print("=> Hoàn tất!\n- Không phát hiện bản cập nhật mới!")
      print("-"*50)
      mbox.showwarning("Thông báo", "Không có bản cập nhật mới!")
   def honNhan1(self):
      print("1.1 BÁT QUÁI HỢP HÔN:")
      print("*Khái niệm: Sự phối hợp của các cung kí sinh (Bát quái) Càn, Khôn, Chấn... gọi là Bát quái hợp hôn sẽ cho ra kết quả cuộc hôn nhân như dưới đây:")
      print("-"*20)
      from tkinter import messagebox
      window = Tk() 
      window.title("Bát quái hợp hôn") 
      window.geometry('400x100+200+200')
      lbl = Label(window, text="Cung bát quái của nam:") 
      lbl.grid(column=0, row=0)
      lbl = Label(window, text="Cung bát quái của nữ:") 
      lbl.grid(column=0, row=1)
      gt1 = Combobox(window); gt1['values']=bq; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=bq; gt2.grid(column=1, row=1)
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
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=1, row=2)
      window.mainloop()
   def honNhan2(self):
      print("1.2: BÁT SAN GIAO CHIẾN")
      print("*Khái niệm: là sự khắc khẩu bất hoà, xung đột triền miên, khi các cung Bát quái phối hợp với nhau.")
      print("-"*20)
      from tkinter import messagebox
      window = Tk() 
      window.title("Bát quái giao chiến") 
      window.geometry('400x100+200+200')
      lbl = Label(window, text="Cung bát quái của nam:") 
      lbl.grid(column=0, row=0)
      lbl = Label(window, text="Cung bát quái của nữ:") 
      lbl.grid(column=0, row=1)
      gt1 = Combobox(window); gt1['values']=bq; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=bq; gt2.grid(column=1, row=1)
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
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=1, row=2)
      window.mainloop()
      print("-"*50)     
   def honNhan3(self):
      print("1.3: BÁT SAN TUYỆT MỆNH")
      print("*Khái niệm: là những cặp xấu nhất, mệnh người này triệt người kia, nhưng tất cả không có nghĩa là một trong hai sẽ tử biệt.\
Tuỳ theo mức xung khắc, nếu nhẹ thì dẫn đến khắc khẩu bất hoà, nặng thì con cái bệnh tật, hư hỏng và là nguyên nhân dẫn đến sự nghèo túng cơ cực.")
      print("-"*20)
      from tkinter import messagebox
      window = Tk() 
      window.title("Bát quái giao chiến") 
      window.geometry('400x100+200+200')
      lbl = Label(window, text="Cung bát quái của nam:") 
      lbl.grid(column=0, row=0)
      lbl = Label(window, text="Cung bát quái của nữ:") 
      lbl.grid(column=0, row=1)
      gt1 = Combobox(window); gt1['values']=bq; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=bq; gt2.grid(column=1, row=1)
      def clicked():
         if gt1.current()==0 and gt2.current()==5 or gt1.current()==5 and gt2.current()==0 or gt1.current()==2 and gt2.current()==4\
            or gt1.current()==4 and gt2.current()==2 or gt1.current()==1 and gt2.current()==6 or gt1.current()==6 and gt2.current()==1\
            or gt1.current()==3 and gt2.current()==7 or gt1.current()==7 and gt2.current()==3:
            mbox.showinfo(kq,"Cung bát quái của hai bạn tạo thành một cặp bát san tuyệt mệnh!")
         elif gt1.current()<0 or gt2.current()<0 or gt1.current()>7 or gt2.current()>7:
            mbox.showerror("Lỗi",e)
         else:
            mbox.showinfo(kq,"Cung bát quái của hai bạn không tạo thành một cặp bát san tuyệt mệnh!")
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=1, row=2)
      window.mainloop()
      print("*Chú ý: đây là cặp xấu nhất, tuy nhiên nếu các can chi mệnh phù hợp thì độ nguy hại giảm thiểu rõ rệt.\
\nNhưng cũng đừng vì sự tương khắc ấy mà những người yêu nhau quá sợ hăi!")
      print("-"*50)   
   def honNhan4(self):
      print("1.4: THIÊN CAN HỢP HÔN")
      from tkinter import messagebox
      window = Tk() 
      window.title("Thiên can hợp hôn") 
      window.geometry('400x200+200+200')
      lbl = Label(window, text="Thiên can của nam:"); lbl.grid(column=0, row=0); lbl = Label(window, text="Thiên can của nữ:"); lbl.grid(column=0, row=1)        
      gt1 = Combobox(window); gt1['values']=can; gt1.grid(column=1, row=0); gt2 = Combobox(window); gt2['values']=can; gt2.grid(column=1, row=1)
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
      btn = Button(window, text="Xác nhận", command=clicked) 
      btn.grid(column=1, row=2)
      window.mainloop() 
   def honNhan5(self):
      print("1.5: ĐỊA CHI HỢP HÔN")
      from tkinter import messagebox
      window = Tk() 
      window.title("Địa chi hợp hôn") 
      window.geometry('400x100+200+200')
      lbl = Label(window, text="Địa chi của nam:") 
      lbl.grid(column=0, row=0)
      lbl = Label(window, text="Địa chi của nữ:") 
      lbl.grid(column=0, row=1)
      gt1 = Combobox(window); gt1['values']=chi; gt1.grid(column=1, row=0)
      gt2 = Combobox(window); gt2['values']=chi; gt2.grid(column=1, row=1)
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
      btn = Button(window, text="Xác nhận", command=clicked); btn.grid(column=1, row=2)
      window.mainloop()
      print("-"*50)      
   def honNhan6(self):
      print("1.6: TỰ KIỂM TRA VIỆC HÔN NHÂN")
      print("*Giới thiệu: Một số nhà toán học am hiểu và có chuyên môn đã đưa ra thang điểm (thang 100) cho việc hôn nhân, cưới hỏi như sau:")
      print("- Tình yêu, sự hoà hợp: +50đ\n- Ngũ hành hợp hôn: +12.5đ\n- Bát quái hợp hôn: +12.5đ\n- Thiên can hợp hôn: +12.5đ\n- Địa chi hợp hôn: +12.5đ\
\n- Bát san giao chiến: -15đ\n- Bát san tuyệt mệnh: -20đ")
      print("*Bây giờ, hãy bắt đầu nhập thông tin của 2 bạn!")
      print("-"*20)
      while True:
         try:
            dem=int(input("*Tình yêu, sự hoà hợp (tự đánh giá: 0-50): "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      if dem<0 or dem>50:
         mbox.showerror("Lỗi",e)
      else:
         print("=> Tổng điểm: +",dem,"đ")
         print("*Ngũ hành hợp hôn:")
         m1=input("- Nhập mạng ngũ hành của nam: ")
         f1=input("- Nhập mạng ngũ hành của nữ: ")
         if (m1 in nh1 and f1 in nh3) or (m1 in nh1 and f1 in nh5):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +12.5đ")
            dem+=12.5
         elif (m1 in nh1 and f1 in nh1):
            s=input("*Hai bạn mạng Kim có giống nhau không (ví dụ: cùng là Thoa Xuyến Kim)? (giống nhau ấn Enter, khác nhau nhấn dấu cách và Enter): ")
            if s==' ':
               print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +0đ")
            elif s=='':
               print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +6.25đ")
               dem+=6.25
            else:
               mbox.showerror("Lỗi",e)
         elif (m1 in nh1 and f1 in nh2) or (m1 in nh1 and f1 in nh4):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +0đ")
         elif (m1 in nh2 and f1 in nh3) or (m1 in nh2 and f1 in nh4):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +12.5đ")
            dem+=12.5
         elif (m1 in nh2 and f1 in nh5) or (m1 in nh2 and f1 in nh2):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +6.25đ")
            dem+=6.25
         elif (m1 in nh2 and f1 in nh1):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +0đ")
         elif (m1 in nh3 and f1 in nh1) or (m1 in nh3 and f1 in nh2):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +12.5đ")
            dem+=12.5
         elif m1 in nh3 and f1 in nh3:
            s=input("*Hai bạn mạng Thuỷ có giống nhau không (ví dụ: cùng là Trường Lưu Thuỷ)? (giống nhau ấn Enter, khác nhau nhấn dấu cách và Enter): ")
            if s==' ':
               print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +0đ")
            elif s=='':
               print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +6.25đ")
               dem+=6.25
            else:
               mbox.showerror("Lỗi",e)  
         elif m1 in nh3 and f1 in nh4:
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +6.25đ")
            dem+=6.25
         elif m1 in nh3 and f1 in nh5:
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +0đ")
         elif (m1 in nh4 and f1 in nh2) or (m1 in nh4 and f1 in nh5):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +12.5đ")
            dem+=12.5
         elif m1 in nh4 and f1 in nh4:
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +6.25đ")
            dem+=6.25
         elif (m1 in nh4 and f1 in nh1) or (m1 in nh4 and f1 in nh3):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +0đ")
         elif (m1 in nh5 and f1 in nh1) or (m1 in nh5 and f1 in nh4):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +12.5đ")
            dem+=12.5
         elif m1 in nh5 and f1 in nh5:
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +6.25đ")
            dem+=6.25
         elif (m1 in nh5 and f1 in nh2) or (m1 in nh5 and f1 in nh3):
            print("=> Nam mệnh",m1,"kết hợp với Nữ mệnh",f1,": +0đ")
         else:
            mbox.showerror("Lỗi",e)  
         print("*Bát quái hợp hôn:")
         bqh=input("- Nhập quẻ bát quái hợp hôn của 2 bạn: ")
         if bqh in bqhh1:
            print("=> Quẻ",bqh,": +12.5đ")
            dem+=12.5
         elif bqh in bqhh2:
            print("=> Quẻ",bqh,": +10.9375đ")
            dem+=10.9375
         elif bqh in bqhh3:
            print("=> Quẻ",bqh,": +9.375đ")
            dem+=9.375
         elif bqh in bqhh4:
            print("=> Quẻ",bqh,": +7.8125đ")
            dem+=7.8125
         elif bqh in bqhh8:
            print("=> Quẻ",bqh,": +6.25đ")
            dem+=6.25
         elif bqh in bqhh7:
            print("=> Quẻ",bqh,": +4.6875đ")
            dem+=4.6875
         elif bqh in bqhh6:
            print("=> Quẻ",bqh,": +3.125đ")
            dem+=3.125
         elif bqh in bqhh5:
            print("=> Quẻ",bqh,": +1.5625đ")
            dem+=1,5625
         else:
            mbox.showerror("Lỗi",e)  
         print("*Thiên can hợp hôn:")
         m2=input("- Nhập thiên can của nam: ")
         f2=input("- Nhập thiên can của nữ: ")
         if (m2 in can0 and f2 in can5) or (m2 in can1 and f2 in can6) or (m2 in can2 and f2 in can7) or (m2 in can3 and f2 in can8)\
            or (m2 in can4 and f2 in can9) or (m2 in can5 and f2 in can0) or (m2 in can6 and f2 in can1) or (m2 in can7 and f2 in can2)\
            or (m2 in can8 and f2 in can3) or (m2 in can9 and f2 in can4):
            print("=> Thiên can nam",m2,"hợp Thiên can nữ",f2,": +12.5đ")
            dem+=12.5
         elif (m2 in can0 and f2 in can4) or (m2 in can1 and f2 in can5) or (m2 in can2 and f2 in can6) or (m2 in can3 and f2 in can7)\
            or (m2 in can4 and f2 in can8) or (m2 in can5 and f2 in can9) or (m2 in can6 and f2 in can0) or (m2 in can7 and f2 in can1)\
            or (m2 in can8 and f2 in can2) or (m2 in can9 and f2 in can3):
            print("=> Thiên can nam",m2,"phá Thiên can nữ",f2,": +6.25đ")
            dem+=6.25
         elif (m2 in can0 and f2 in can6) or (m2 in can1 and f2 in can7) or (m2 in can2 and f2 in can8) or (m2 in can3 and f2 in can9)\
            or (m2 in can4 and f2 in can0) or (m2 in can5 and f2 in can1) or (m2 in can6 and f2 in can2) or (m2 in can7 and f2 in can3)\
            or (m2 in can8 and f2 in can4) or (m2 in can9 and f2 in can5):
            print("=> Thiên can nam",m2,"xung khắc Thiên can nữ",f2,": +3.125đ")
            dem+=3.125
         else:
            print("=> Thiên can nam",m2,"và Thiên can nữ",f2,": +9.375đ")
            dem+=9.375
         print("*Địa chi hợp hôn:")
         m3=input("- Nhập địa chi của nam: ")
         f3=input("- Nhập địa chi của nữ: ")
         if (m3 in chi1 and f3 in chi2) or (m3 in chi2 and f3 in chi1) or (m3 in chi3 and f3 in chi0) or (m3 in chi0 and f3 in chi3)\
            or (m3 in chi4 and f3 in chi11) or (m3 in chi11 and f3 in chi4) or (m3 in chi5 and f3 in chi10) or (m3 in chi10 and f3 in chi5)\
            or (m3 in chi6 and f3 in chi9) or (m3 in chi9 and f3 in chi6) or (m3 in chi7 and f3 in chi8) or (m3 in chi8 and f3 in chi7):
            print("=> Địa chi nam",m3,"kết hợp với Địa chi nữ",f3,": +12.5đ")
            dem+=12.5
         else:
            print("=> Địa chi nam",m3,"kết hợp với Địa chi nữ",f3,": +6.25đ")
            dem+=6.25
         print("*Bát san giao chiến & Bát san tuyệt mệnh:")
         m4=input("Nhập cung bát quái của nam: ")
         f4=input("Nhập cung bát quái của nữ: ")
         if (m4 in bq1 and f4 in bq5) or (m4 in bq1 and f4 in bq7) or (m4 in bq5 and f4 in bq1) or (m4 in bq7 and f4 in bq1) or (m4 in bq7 and f4 in bq3)\
            or (m4 in bq3 and f4 in bq7) or (m4 in bq7 and f4 in bq4) or (m4 in bq4 and f4 in bq7) or (m4 in bq8 and f4 in bq6) or (m4 in bq6 and f4 in bq8)\
            or (m4 in bq4 and f4 in bq5) or (m4 in bq5 and f4 in bq4) or (m4 in bq6 and f4 in bq7) or (m4 in bq7 and f4 in bq6) or (m4 in bq2 and f4 in bq6)\
            or (m4 in bq6 and f4 in bq2):
            print("=> Cung bát quái",m4,"và cung bát quái",f4,"tạo thành một cặp bát san giao chiến: -15đ")
            dem-=15
         elif (m4 in bq1 and f4 in bq6) or (m4 in bq6 and f4 in bq1) or (m4 in bq3 and f4 in bq5) or (m4 in bq5 and f4 in bq3) or (m4 in bq2 and f4 in bq7)\
            or (m4 in bq7 and f4 in bq2):
            print("*Bát san tuyệt mệnh:")
            print("=> Cung bát quái",m4,"và cung bát quái",f4,"tạo thành một cặp bát san tuyệt mệnh: -15đ")
            dem-=15
         elif (m4 in bq7 and f4 in bq4) or (m4 in bq4 and f4 in bq7):
            print("=> Cung bát quái",m4,"và cung bát quái",f4,"tạo thành một cặp bát san tuyệt mệnh: -20đ")
            dem-=20
         else:
            print("=> Cung bát quái",m4,"và",f4,"của hai bạn không phải là một cặp bát san giao chiến hoặc bát san tuỵệt mệnh!")
         if dem<101 and dem>=0:
            print("*Sau tất cả, tổng điểm của hai bạn là:",dem,"đ!")
            if dem<100 and dem>=95:
               mbox.showinfo("Kết quả", "Đánh giá: S (Lí tưởng)\n=>  Xin chúc mừng! Hai bạn đă đạt được số điểm tốt nhất! Hai bạn là một cặp đôi lí tưởng!")
            elif dem<95 and dem>=75:
               mbox.showinfo("Kết quả", "Đánh giá: A (Tốt)")
            elif dem<75 and dem>=55:
               mbox.showinfo("Kết quả", "Đánh giá: B (Khá)")
            elif dem<55 and dem>=45:
               mbox.showinfo("Kết quả", "Đánh giá: C (Trung bình)\n=> Hai bạn chỉ có tình yêu, sự hoà hợp hoặc chỉ có các yếu tố siêu hình")
            elif dem<45 and dem>=40:
               mbox.showinfo("Kết quả", "Đánh giá: D\n=> Dễ phiêu lưu trong việc hôn nhân")
            elif dem<40 and dem>=25:
               mbox.showinfo("Kết quả", "Đánh giá: E\n=> Hạnh phúc bị nhiều yếu tố đe doạ")
            elif dem<25 and dem>=0:
               mbox.showinfo("Kết quả", "Đánh giá: F\n=> Hạnh phúc luôn bên bờ vực")
         else:
            mbox.showerror("Lỗi","Oops! Đă xảy ra lỗi trong quá trình nhập dữ liệu")
      print("-"*50)
   def honNhan7(self):
      print("1.7: CHỌN NGÀY TỐT TRONG HÔN NHÂN")
      m=int(input("Nhập tháng bạn dự định cử hành hôn lễ: "))
   def honNhan8(self):
      print("1.8: CHỌN THÁNG TỐT TRONG HÔN NHÂN (mục này chỉ dành cho bên nhà gái)")
      print("*Chú thích: tính chất (tháng)\n- Đại lợi: tốt cho con gái xuất giá\n- Phòng Phu chủ: kỵ với chồng\n- Phòng Thê chủ: kỵ với bản thân\
\n- Phòng Công cô: kỵ với cha mẹ chồng\n- Phòng Nữ phụ mẫu: kỵ với cha mẹ ruột")
      print("+ Nếu trai gái mồ côi thì không sợ tháng kỵ phòng Công cô, phòng Nữ phụ mẫu.\n+ Tiểu lợi: kỵ với bà Mai (còn gọi là phòng Mai nhân),\
nếu không có bà Mai hay chỉ mượn làm giúp lễ cho đủ thì không ngại gì.")
      print("-"*20)
      x=input("*Nhập tuổi (con giáp) người nữ kết hôn: ")
      dl=" - Đại lợi:"; tl="- Tiểu lợi:"; pcc="- Phòng Công cô:"; ppm="- Phòng Nữ phụ mẫu:"; ppc="- Phòng Phu chủ:"; ptc="- Phòng Thê chủ:"
      t1="1, 7\n"; t2="2, 8\n"; t3="3, 9\n"; t4="4, 10\n"; t5="5, 11\n"; t6="6, 12\n"
      print("(các số từ 1-12 là các tháng trong năm)")
      if x in chi1 or x in chi7:
         print(dl,t6,tl,t1,pcc,t2,ppm,t3,ppc,t4,ptc,t5)
      elif x in chi2 or x in chi8:
         print(dl,t5,tl,t4,pcc,t3,ppm,t2,ppc,t4,ptc,t6)
      elif x in chi3 or x in chi9:
         print(dl,t2,tl,t3,pcc,t4,ppm,t5,ppc,t6,ptc,t1)
      elif x in chi4 or x in chi10:
         print(dl,t1,tl,t6,pcc,t5,ppm,t4,ppc,t3,ptc,t2)
      elif x in chi5 or x in chi11:
         print(dl,t4,tl,t5,pcc,t6,ppm,t1,ppc,t2,ptc,t3)
      elif x in chi6 or x in chi0:
         print(dl,t3,tl,t2,pcc,t1,ppm,t6,ppc,t5,ptc,t4)
      else:
         mbox.showerror("Lỗi",e)
      print("-"*50)   
   def nguHanh1(self):
      from tkinter import messagebox
      window = Tk() 
      window.title("Tra ngũ hành theo năm can chi") 
      window.geometry('400x100+200+200')
      lbl = Label(window, text="Năm sinh âm lịch của bạn:") 
      lbl.grid(column=0, row=0)      
      gt = Combobox(window) 
      gt['values']=canchi
      gt.grid(column=1, row=0)
      def clicked():
         if gt.current()==0 or gt.current()==5:
            mbox.showinfo(kq,"Mạng: Hải Trung Kim (vàng giữa biển)\nkhắc Bình Địa Mộc (cây sát đất)")
         elif gt.current()==10 or gt.current()==15:
            mbox.showinfo(kq,"Mạng: Lư Trung Hoả (lửa trong lò)\nkhắc: Kiếm Phong Kim (mũi kiếm vàng)")
         elif gt.current()==20 or gt.current()==25:
            mbox.showinfo(kq,"Mạng: Đại Lâm Mộc (cây rừng lớn)\nkhắc: Đại Trạch Thổ (đất nhà lớn)")       
         elif gt.current()==30 or gt.current()==35:
            mbox.showinfo(kq,"Mạng: Lộ Bàn Thổ (đất đường đi)\nkhắc: Tuyền Trung Thuỷ (nước trong suối)")
         elif gt.current()==40 or gt.current()==45:
            mbox.showinfo(kq,"Mạng: Kiếm Phong Kim (mũi kiếm vàng)\nkhắc: Phúc Đăng Hoả (lửa che đèn)")
         elif gt.current()==50 or gt.current()==55:
            mbox.showinfo(kq,"Mạng: Sơn Đầu Hoả (lửa đầu núi)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif gt.current()==1 or gt.current()==6:
            mbox.showinfo(kq,"Mạng: Giang Hạ Thuỷ (nước dưới sông)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif gt.current()==11 or gt.current()==16:
            mbox.showinfo(kq,"Mạng: Thành Đầu Thổ (đất trên thành)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif gt.current()==21 or gt.current()==26:
            mbox.showinfo(kq,"Mạng: Bạch Lạp Kim (vàng nến trắng)\nkhắc: Phúc Đăng Hoả (lửa che đèn)")
         elif gt.current()==31 or gt.current()==36:
            mbox.showinfo(kq,"Mạng: Dương Liễu Mộc (cây dương liễu)\nkhắc: Lộ Bàn Thổ (đất đường đi)")
         elif gt.current()==41 or gt.current()==46:
            mbox.showinfo(kq,"Mạng: Tuyền Trung Thuỷ (nước trong suối)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif gt.current()==51 or gt.current()==56:
            mbox.showinfo(kq,"Thổ: Ốc Thượng Thổ (đất trên nhà)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif gt.current()==2 or gt.current()==7:
            mbox.showinfo(kq,"Mạng: Tích Lịch Hoả (lửa sấm sét)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif gt.current()==12 or gt.current()==17:
            mbox.showinfo(kq,"Mạng: Tùng Bá Mộc (cây tùng bách)\nkhắc: Lộ Bàn Thổ (đất đường đi)")
         elif gt.current()==22 or gt.current()==27:
            mbox.showinfo(kq,"Mạng: Trường Lưu Thuỷ (nước chảy dài)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif gt.current()==32 or gt.current()==37:
            mbox.showinfo(kq,"Mạng: Sa Trung Kim (vàng trong cát)\nkhắc: Thạch Lựu Mộc (cây thạch lựu)")
         elif gt.current()==42 or gt.current()==47:
            mbox.showinfo(kq,"Mạng: Sơn Hạ Hoả (lửa dưới núi)\nkhắc: Tích Lịch Hoả (lửa sấm sét)")
         elif gt.current()==52 or gt.current()==57:
            mbox.showinfo(kq,"Mạng: Bình Địa Mộc (cây sát đất)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif gt.current()==3 or gt.current()==8:
            mbox.showinfo(kq,"Mạng: Bích Thượng Thổ (đất trên tường)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif gt.current()==13 or gt.current()==18:
            mbox.showinfo(kq,"Mạng: Kim Bạch Kim (vàng trắng vàng)\nkhắc: Lư Trung Hoả (lửa trong lò)")
         elif gt.current()==23 or gt.current()==28:
            mbox.showinfo(kq,"Mạng: Phúc Đăng Hoả (lửa che đèn)\nkhắc: Thoa Xuyến Kim (vàng trang sức)")
         elif gt.current()==33 or gt.current()==38:
            mbox.showinfo(kq,"Mạng: Thiên Hà Thuỷ (nước sông trời)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
         elif gt.current()==43 or gt.current()==48:
            mbox.showinfo(kq,"Mạng: Đại Trạch Thổ (đất nhà lớn)\nkhắc: Thiên Hà Thuỷ (nước sông trời)")
         elif gt.current()==53 or gt.current()==58:
            mbox.showinfo(kq,"Mạng: Thoa Xuyến Kim (vàng trang sức)\nkhắc: Đại Lâm Mộc (cây rừng lớn)")
         elif gt.current()==4 or gt.current()==9:
            mbox.showinfo(kq,"Mạng: Tang Đố Mộc (cây dâu tằm)\nkhắc: Thành Đầu Thổ (đất trên thành)")
         elif gt.current()==14 or gt.current()==19:
            mbox.showinfo(kq,"Mạng: Đại Khê Thuỷ (nước suối lớn)\nkhắc: Sơn Hạ Hoả (lửa dưới núi)")
         elif gt.current()==24 or gt.current()==29:
            mbox.showinfo(kq,"Mạng: Thiên Thượng Hoả (lửa trên trời)\nkhắc: Sa Trung Kim (vàng trong cát)")
         elif gt.current()==34 or gt.current()==39:
            mbox.showinfo(kq,"Mạng: Sa Trung Thổ (đất trong cát)\nkhắc: Dương Liễu Mộc (cây dương liễu)")
         elif gt.current()==43 or gt.current()==49:
            mbox.showinfo(kq,"Mạng: Thạch Lựu Mộc (cây thạch lựu)\nkhắc: Bích Thượng Thổ (đất trên tường)")
         elif gt.current()==54 or gt.current()==59:
            mbox.showinfo(kq,"Mạng: Đại Hải Thuỷ (nước biển lớn)\nkhắc: Thiên Thượng Hoả (lửa trên trời)")
      btn = Button(window, text="Xác nhận", command=clicked) 
      btn.grid(column=2, row=0)
      window.mainloop()
   def nguHanh3(self):
      print("2.3: CÁC NGUYÊN TẮC NGŨ HÀNH CHẾ HÓA:")
      print("- Nguyên tắc 1:")
      print("Kim do Thổ sinh ra, Thổ nhiều thì Kim bị chôn lấp")
      print("Mộc do Thủy sinh, Thủy nhiều thì Mộc bị trôi nổi phiêu bạt")
      print("Thổ do Hỏa sinh ra, Hỏa nhiều thì Thổ bị cháy tiêu")
      print("Thuỷ do Kim sinh ra, Kim nhiều thì nước bị đục")
      print("Hỏa do Mộc sinh sinh ra, Mộc nhiều thì Hỏa càng sáng tỏ.")
      print("- Nguyên tắc 2: Tương sinh")
      print("Kim sinh Thủy, Thuỷ nhiều thì Kim bị chìm mất")
      print("Thuỷ sinh Mộc, Mộc nhiều thì Thủy bị cạn (thu rút lại)")
      print("Mộc sinh Hỏa, Hỏa nhiều thì Mộc bị cháy hết")
      print("Hỏa sinh Thổ, Thổ nhiều thì Hỏa tối lại")
      print("Thổ sinh Kim, Kim nhiều thì Thổ yếu (mất nhiều năng lực)")
      print("- Nguyên tắc 3:")
      print("Kim suy (ít) gặp Hỏa, tất bị đun, chảy ra")
      print("Hỏa yếu gặp Thủy, tất bị tắt, tiêu diệt")
      print("Thủy yếu (ít) gặp Thổ, tất bị ứ tắc")
      print("Thổ suy (ít) gặp Mộc, tất gặp sự đảo lộn bế hãm (mất tính chất nguyên thủy)")
      print("Mộc yếu gặp Kim, tất bị chém gãy.")
      print("– Nguyên tắc 4:")
      print("Kim mạnh (nhiều) được Thủy, sự nhọn sắc mòn gãy bớt đi")
      print("Thuỷ mạnh (nhiều) được Mộc, thế sức mạnh bị tiết bớt đi")
      print("Mộc mạnh (nhiều) được Hỏa, sự cứng rắn bị hóa giải bớt đi")
      print("Hỏa mạnh (nhiều) được Thổ, sự sáng rực bị giữ bớt lại")
      print("Thổ mạnh (nhiều) được Kim, sự ủng hộ (giúp sức) bị chế bớt lại")
      print("- Nguyên tắc 5: Tương khắc")
      print("Kim khắc Mộc, nhưng Mộc rắn thì Kim gãy, sứt mẻ")
      print("Mộc khắc Thổ, nhưng Thổ nhiều, nặng thì Mộc gãy")
      print("Thổ khắc Thủy, nhưng Thủy nhiều thì Thổ bị trôi đi")
      print("Thủy khắc Hỏa, nhưng Hỏa bốc cháy lớn, thì Thủy bị cạn bốc hơi đi")
      print("Hỏa khắc Kim, nhưng Kim nhiều chảy tràn ra thì Hỏa tắt.")
      print("-"*50) 
   def batQuai1(self):
      print("3.1: BÁT QUÁI THEO NĂM SINH DƯƠNG LỊCH")
      print("*Giới thiệu: Có trên có dưới, có tả có hữu, có trước có sau nên gọi là Vũ. Có xưa có nay, có quá khứ có tương lai nên gọi là Trụ.\
Trong Vũ trụ có ánh sáng, tối tăm, ngày đêm, mưa gió, sấm chớp, sông hồ, ao rạch... nên luận thành Bát Quái gồm có:\n",bq)
      print("-"*20)
      while True:
         try:
            y=int(input("*Nhập năm sinh của bạn: "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      if y<1:
         mbox.showerror("Lỗi",e)
      x=y%10
      z=y%12
      if (x==y==1) or (x==y==7) or (x==3 and z==11) or (x==8 and z==4) or (x==0 and z==4) or (x==4 and z==2) or (x==6 and z==10):
         print("=>",bq[0].upper(),"\n- Hướng: Tây Bắc\n- Tượng trưng: Trời, mặt trời, ban ngày, ánh sáng, cha, phái nam\n- Thuộc: dương Kim")
      elif (x==y==0) or (x==9 and z==7) or (x==4 and z==0) or (x==3 and z==9) or (x==6 and z==0) or (x==1 and z==4) or (x==7 and z==9) or (x==2 and z==0) or (x==9 and z==7):
         print("=>",bq[6].upper(),"\n- Hướng: Tây Nam\n- Tượng trưng: Đất, mặt trăng, ban đêm, bóng tối, mẹ, phái nữ\n- Thuộc: âm Thổ")
      elif (x==z==4) or (x==0 and z==8) or (x==5 and z==1) or (x==7 and z==1) or (x==2 and z==4) or (x==8 and z==10) or (x==3 and z==1):
         print("=>",bq[3].upper(),"\n- Hướng: chính Đông\n- Tượng trưng: sấm sét, con trai trưởng\n- Thuộc: dương Mộc")
      elif (x==z==5) or (x==1 and z==9) or (x==6 and z==2) or (x==8 and z==2) or (x==3 and z==5) or (x==9 and z==11):
         print("=>",bq[4].upper(),"\n- Hướng: Đông Nam\n- Tượng trưng: gió băo, con gái trưởng\n- Thuộc: âm Mộc")
      elif (x==z==6) or (x==8 and z==6) or (x==2 and z==8) or (x==5 and z==11) or (x==4 and z==8) or (x==0 and z==2) or (x==6 and z==8) or (x==1 and z==11):
         print("=>",bq[1].upper(),"\n- Hướng: chính Bắc\n- Tượng trưng: nước, con trai thứ\n- Thuộc: dương Thuỷ")
      elif (x==7 and z==5) or (x==2 and z==10) or (x==1 and z==7) or (x==4 and z==10) or (x==3 and z==7) or (x==9 and z==1) or (x==5 and z==7) or (x==0 and z==10):
         print("=>",bq[5].upper(),"\n- Hướng: chính Nam\n- Tượng trưng: lửa, con gái thứ\n- Thuộc: âm Hoả")
      elif (x==y==3) or (x==z==9) or (x==6 and z==4) or (x==7 and z==3) or (x==0 and z==6) or (x==9 and z==3) or (x==2 and z==6) or (x==8 and z==0) or (x==4 and z==6):
         print("=>",bq[2].upper(),"\n- Hướng: Đông Bắc\n- Tượng trưng: núi non, con trai út\n- Thuộc: dương Thổ")
      else:
         print("=>",bq[7].upper(),"\n- Hướng: chính Tây\n- Tượng trưng: ao hồ, sông rạch, con gái út\n- Thuộc: âm Kim")
      print("-"*20)
      print("*Chú ý: đây là cung Bát quái (cung Ký sinh), loại cung về vận mệnh đặc điểm của từng người, vận hạn cứ theo đó mà định hình.\
Còn loại cung còn lại (cung Bát trạch) chỉ là cung liên quan đến điền thổ, đến chỗ ở, việc xây cất nhà cửa, có sự phân biệt giữa nam và nữ, không nên nhầm lẫn.")
      print("-"*50) 
   def batQuai2(self):
      from tkinter import messagebox
      window = Tk() 
      window.title("Địa chi (con giáp)") 
      window.geometry('700x200+200+200')
      lbl=Label(window, text="Năm sinh âm lịch của bạn:")
      lbl.grid(column=0, row=0)
      gt=Combobox(window) 
      gt['values']=canchi
      gt.grid(column=1, row=0)
      def clicked():
         lbl = Label(window, text="Kết quả:")
         lbl.grid(column=0, row=2)
         lbl = Label(window, text=" ")
         lbl.grid(column=0, row=1)
         txt = scrolledtext.ScrolledText(window,width=50,height=5)
         txt.grid(column=1, row=2)
         if gt.current()==2 or gt.current()==3 or gt.current()==15 or gt.current()==33 or gt.current==36 or gt.current()==49 or gt.current()==50:
            txt.insert(INSERT,"*Cung: Càn\n- Hướng: Tây Bắc\n- Tượng trưng: Trời, mặt trời, ban ngày, ánh sáng, cha, phái nam\n- Thuộc: dương Kim")
         elif gt.current()==10 or gt.current()==22 or gt.current()==23 or gt.current()==24 or gt.current==37 or gt.current()==53:
            txt.insert(INSERT,"*Cung: Khảm\n- Hướng: chính Bắc\n- Tượng trưng: nước, con trai thứ\n- Thuộc: dương Thuỷ")
         elif gt.current()==1 or gt.current()==12 or gt.current()==13 or gt.current()==14 or gt.current()==25 or gt.current()==44 or gt.current()==56\
              or gt.current==57 or gt.current==59:
            txt.insert(INSERT,"*Cung: Cấn\n- Hướng: Đông Bắc\n- Tượng trưng: núi non, con trai út\n- Thuộc: dương Thổ")
         elif gt.current()==0 or gt.current()==4 or gt.current()==5 or gt.current()==21 or gt.current==34 or gt.current()==39 or gt.current()==45\
            or gt.current()==46 or gt.current()==47:
            txt.insert(INSERT,"*Cung: Chấn\n- Hướng: chính Đông\n- Tượng trưng: sấm sét, con trai trưởng\n- Thuộc: dương Mộc")
         elif gt.current()==9 or gt.current()==26 or gt.current==35 or gt.current()==51 or gt.current()==52:
            txt.insert(INSERT,"*Cung: Tốn\n- Hướng: Đông Nam\n- Tượng trưng: gió băo, con gái trưởng\n- Thuộc: âm Mộc")
         elif gt.current()==6 or gt.current()==17 or gt.current()==18 or gt.current()==30 or gt.current()==31 or gt.current()==48:
            txt.insert(INSERT,"*Cung: Ly\n- Hướng: chính Nam\n- Tượng trưng: lửa, con gái thứ\n- Thuộc: âm Hoả")
         elif gt.current()==11 or gt.current()==16 or gt.current==19 or gt.current()==27 or gt.current()==29 or gt.current()==40 or gt.current()==41\
            or gt.current()==42 or gt.current()==43 or gt.current()==58:
            txt.insert(INSERT,"*Cung: Khôn\n- Hướng: Tây Nam\n- Tượng trưng: Đất, mặt trăng, ban đêm, bóng tối, mẹ, phái nữ\n- Thuộc: âm Thổ")
         elif gt.current()==7 or gt.current()==8 or gt.current()==20 or gt.current()==28 or gt.current()==38 or gt.current()==54 or gt.current()==55:
            txt.insert(INSERT,"*Cung: Đoài\n- Hướng: chính Tây\n- Tượng trưng: ao hồ, sông rạch, con gái út\n- Thuộc: âm Kim")
         else:
            mbox.showerror("Lỗi",e)
      btn = Button(window, text="Xác nhận", command=clicked) 
      btn.grid(column=2, row=0)
      window.mainloop() 
      print("*Chú ý: đây là cung Bát quái (cung Ký sinh), loại cung về vận mệnh đặc điểm của từng người, vận hạn cứ theo đó mà định hình.\
Còn loại cung còn lại (cung Bát trạch) chỉ là cung liên quan đến điền thổ, đến chỗ ở, việc xây cất nhà cửa, có sự phân biệt giữa nam và nữ, không nên nhầm lẫn.")
      print("-"*50) 
   def thienCan(self):
      from tkinter import messagebox
      window = Tk() 
      window.title("Thiên can") 
      window.geometry('400x200+200+200')
      lbl = Label(window, text="Thiên can của bạn:") 
      lbl.grid(column=0, row=0)      
      thiencan = Combobox(window) 
      thiencan['values']=can
      thiencan.grid(column=1, row=0)
      def clicked():
         lbl = Label(window, text="Kết quả:")
         lbl.grid(column=0, row=2)
         lbl = Label(window, text=" ")
         lbl.grid(column=0, row=1)
         txt = scrolledtext.ScrolledText(window,width=20,height=5)
         txt.grid(column=1,row=2)
         if thiencan.current()==0:
            txt.insert(INSERT,'- Thuộc tính: Dương\n- Ngũ hành: Mộc\n- Hợp: Kỷ\n- Phá: Mậu\n- Xung: Canh')
         elif thiencan.current()==1:            
            txt.insert(INSERT,'- Thuộc tính: Âm\n- Ngũ hành: Mộc\n- Hợp: Canh\n- Phá: Kỷ\n- Xung: Tân')
         elif thiencan.current()==2:            
            txt.insert(INSERT,'- Thuộc tính: Dương\n- Ngũ hành: Hoả\n- Hợp: Tân\n- Phá: Canh\n- Xung: Nhâm')
         elif thiencan.current()==3:            
            txt.insert(INSERT,'- Thuộc tính: Âm\n- Ngũ hành: Hoả\n- Hợp: Nhâm\n- Phá: Tân\n- Xung: Quý')
         elif thiencan.current()==4:            
            txt.insert(INSERT,'- Thuộc tính: Dương\n- Ngũ hành: Thổ\n- Hợp: Quý\n- Phá: Nhâm\n- Xung: Giáp')
         elif thiencan.current()==5:            
            txt.insert(INSERT,'- Thuộc tính: Âm\n- Ngũ hành: Thổ\n- Hợp: Giáp\n- Phá: Quý\n- Xung: Ất')
         elif thiencan.current()==6:            
            txt.insert(INSERT,'- Thuộc tính: Dương\n- Ngũ hành: Kim\n- Hợp: Ất\n- Phá: Giáp\n- Xung: Bính')
         elif thiencan.current()==7:            
            txt.insert(INSERT,'- Thuộc tính: Âm\n- Ngũ hành: Kim\n- Hợp: Bính\n- Phá: Ất\n- Xung: Đinh')
         elif thiencan.current()==8:            
            txt.insert(INSERT,'- Thuộc tính: Dương\n- Ngũ hành: Thuỷ\n- Hợp: Đinh\n- Phá: Bính\n- Xung: Mậu')
         elif thiencan.current()==9:            
            txt.insert(INSERT,'- Thuộc tính: Âm\n- Ngũ hành: Thuỷ\n- Hợp: Mậu\n- Phá: Đinh\n- Xung: Kỷ')
         else:
            mbox.showerror("Lỗi",e)
      btn = Button(window, text="Xác nhận", command=clicked) 
      btn.grid(column=2, row=0)
      window.mainloop() 
   def diaChi1(self):
      from tkinter import messagebox
      window = Tk() 
      window.title("Địa chi (con giáp)") 
      window.geometry('500x200+200+200')
      lbl=Label(window, text="Địa chi (con giáp) của bạn:") 
      lbl.grid(column=0, row=0)      
      diachi=Combobox(window) 
      diachi['values']=chi
      diachi.grid(column=1, row=0)
      def clicked():
         lbl = Label(window, text="Kết quả:")
         lbl.grid(column=0, row=2)
         lbl = Label(window, text=" ")
         lbl.grid(column=0, row=1)
         txt = scrolledtext.ScrolledText(window,width=30,height=5)
         txt.grid(column=1, row=2)
         if diachi.current()==0:
            txt.insert(INSERT,'* Thuộc tính: Dương\n* Ngũ hành: Thuỷ\n* Nhị hợp: Tý - Sửu\n* Tam hợp: Thân - Tý - Thìn\n* Lục xung: Tý - Ngọ')
         elif diachi.current()==1:
            txt.insert(INSERT,'* Thuộc tính: Âm\n* Ngũ hành: Thổ\n* Nhị hợp: Tý - Sửu\n* Tam hợp: Tỵ - Dậu - Sửu\n* Lục xung: Mùi - Sửu')
         elif diachi.current()==2:
            txt.insert(INSERT,'* Thuộc tính: Dương\n* Ngũ hành: Mộc\n* Nhị hợp: Dần - Hợi\n* Tam hợp: Dần - Ngọ - Tuất\n* Lục xung: Thân - Dần')
         elif diachi.current()==3:
            txt.insert(INSERT,'* Thuộc tính: Âm\n* Ngũ hành: Mộc\n* Nhị hợp: Măo/Mẹo - Tuất\n* Tam hợp: Hợi - Măo/Mẹo - Mùi\n* Lục xung: Măo/Mẹo - Dậu')
         elif diachi.current()==4:
            txt.insert(INSERT,'* Thuộc tính: Dương\n* Ngũ hành: Thổ\n* Nhị hợp: Thìn - Dậu\n* Tam hợp: Thân - Tý - Thìn\n* Lục xung: Thìn - Tuất')
         elif diachi.current()==5:
            txt.insert(INSERT,'* Thuộc tính: Âm\n* Ngũ hành: Hoả\n* Nhị hợp: Tỵ - Thân\n* Tam hợp: Tỵ - Dậu - Sửu\n* Lục xung: Hợi - Tỵ')
         elif diachi.current()==6:
            txt.insert(INSERT,'* Thuộc tính: Dương\n* Ngũ hành: Hoả\n* Nhị hợp: Ngọ - Mùi\n* Tam hợp: Dần - Ngọ - Tuất\n* Lục xung: Tý - Ngọ')
         elif diachi.current()==7:
            txt.insert(INSERT,'* Thuộc tính: Âm\n* Ngũ hành: Thổ\n* Nhị hợp: Ngọ - Mùi\n* Tam hợp: Hợi - Măo/Mẹo - Mùi\n* Lục xung: Mùi - Sửu')
         elif diachi.current()==8:
            txt.insert(INSERT,'* Thuộc tính: Dương\n* Ngũ hành: Kim\n* Nhị hợp: Tỵ - Thân\n* Tam hợp: Thân - Tý - Thìn\n* Lục xung: Thân - Dần')
         elif diachi.current()==9:
            txt.insert(INSERT,'* Thuộc tính: Âm\n* Ngũ hành: Kim\n* Nhị hợp: Thìn - Dậu\n* Tam hợp: Tỵ - Dậu - Sửu\n* Lục xung: Măo/Mẹo - Dậu')
         elif diachi.current()==10:
            txt.insert(INSERT,'* Thuộc tính: Dương\n* Ngũ hành: Thổ\n* Nhị hợp: Măo/Mẹo - Tuất\n* Tam hợp: Dần - Ngọ - Tuất\n* Lục xung: Thìn - Tuất')
         elif diachi.current()==11:
            txt.insert(INSERT,'* Thuộc tính: Âm\n* Ngũ hành: Thuỷ\n* Nhị hợp: Dần - Hợi\n* Tam hợp: Hợi - Măo/Mẹo - Mùi\n* Lục xung: Hợi - Tỵ')
         else:
            mbox.showerror("Lỗi",e)
      btn = Button(window, text="Xác nhận", command=clicked) 
      btn.grid(column=2, row=0)
      window.mainloop()
   def duongLich1(self):
      print("6.1: TRA THỨ TỰ NGÀY, TUẦN TRONG NĂM")
      print("-"*50)
      while True:
         try:
            y=int(input("*Nhập năm: "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      if y<1: 
         mbox.showerror("Lỗi",e)
      else:
         m = int(input("*Nhập tháng: "))
         if m<1 or m>12:
            mbox.showerror("Lỗi",e)
         else:
            d = int(input("*Nhập ngày: "))
            if d<1 or d>31 or (y%400!=0 and m==2 and d>29):
               mbox.showerror("Lỗi",e)
            else:
               d2=d
    #Tính thời gian nhập vào là ngày, tuần thứ mấy trong năm:
               if y%400==0:
                  a=29
               else:
                  a=28
               if m==1:
                     d=d
               else:
                  if m==2:
                     d=31+d
                  elif m==3:
                     d=31+a+d
                  elif m==4:
                     d=31+a+31+d
                  elif m==5:
                     d=31+a+31+30+d
                  elif m==6:
                     d=31+a+31+30+31+d
                  elif m==7:
                     d=31+a+31+30+31+30+d
                  elif m==8:
                     d=31+a+31+30+31+30+31+d
                  elif m==9:
                     d=31+a+31+30+31+30+31+31+d
                  elif m==10:
                     d=31+a+31+30+31+30+31+31+30+d
                  elif m==11:
                     d=31+a+31+30+31+30+31+31+30+31+d
                  else:
                     d=31+a+31+30+31+30+31+31+30+31+30+d
                  w=math.ceil(d/7)
                  print("=> Ngày thứ",d,"trong năm")
                  print("=> Tuần thứ",w,"trong năm")
      print("-"*50) 
   def duongLich2(self):
      print("6.2: TRA THỨ TRONG TUẦN") #đang có bug
      while True:
         try:
            y=int(input("*Nhập năm: "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      if y<1: 
         mbox.showerror("Lỗi",e)
      else:
         m = int(input("*Nhập tháng: "))
         if m<1 or m>12:
            mbox.showerror("Lỗi",e)
         else:
            d = int(input("*Nhập ngày: "))
            if d<1 or d>31 or (y%400!=0 and m==2 and d>29):
                mbox.showerror("Lỗi",e)
            else:
                d=d
      Thu=(d+2*m+(3*(m+1))/5+y+(y/4))%7
      if (m<3):
         m+=12
         y-=1
      if math.ceil(Thu)==1:
         print("=> Chủ nhật")
      else:
         print("=> Thứ: ",math.ceil(Thu))
      print("-"*50) 
   def amLich(self):
      print("7: ÂM LỊCH")
      print("- Năm\n- Tháng\n- Ngày\n- Giờ")
      print("-"*50)
      while True:
         try:
            y=int(input("*Nhập năm: "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      x=y%10
      z=y%12
      if y<1:
         mbox.showerror("Lỗi",e)
      if x==0:
         a=can[7]
      elif x==1:
         a=can[8]
      elif x==2:
         a=can[9]
      elif x==3:
         a=can[0]
      elif x==4:
         a=can[1]
      elif x==5:
         a=can[2]
      elif x==6:
         a=can[3]
      elif x==7:
         a=can[4]
      elif x==8:
         a=can[5]
      else:
         a=can[6]
      if z==0:
         b=chi[9]
      elif z==1:
         b=chi[10]
      elif z==2:
         b=chi[11]
      elif z==3:
         b=chi[0]
      elif z==4:
         b=chi[1]
      elif z==5:
         b=chi[2]
      elif z==6:
         b=chi[3]
      elif z==7:
         b=chi[4]
      elif z==8:
         b=chi[5]
      elif z==9:
         b=chi[6]
      elif z==10:
         b=chi[7]
      else:
         b=chi[8]
      print("=> Năm can chi là: ",a,b)
      while True:
         try:
            m=int(input("*Nhập tháng: "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
         if m<1 or m>12:
            mbox.showerror("Lỗi",e)
      print("-"*50)
   def nguDe1(self):
      print("8.1: TRA NGŨ ĐẾ THEO NĂM SINH DƯƠNG LỊCH")
      while True:
         try:
            y=int(input(iny))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      r=y%60
      if y<1:
         mbox.showerror("Lỗi",e)
      if r==52 or r==53:
         print("=>",ngude[0],": quan lộc, vất vả")
      elif r==8 or r==9 or r==22 or r==30 or r==31:
         print("=>",ngude[0],": trường mạng")
      elif r==23 or r==38 or r==39:
         print("=>",ngude[0],": hiền từ, phú quý")
      elif r==0 or r==1:
         print("=>",ngude[0],": cô bần")
      elif r==18 or r==19 or r==26 or r==27 or r==56 or r==57:
         print("=>",ngude[1],": phú quý")
      elif r==40 or r==41:
         print("=>",ngude[1],": quan lộc, bần hàn")
      elif r==10 or r==11:
         print("=>",ngude[1],": cô bần")
      elif r==48 or r==49:
         print("=>",ngude[1],": quan lộc")
      elif r==4 or r==5 or r==12 or r==13 or r==35 or r==42 or r==43 or r==50:
         print("=>",ngude[2],": phú quý")
      elif r==20 or r==21:
         print("=>",ngude[2],": trường mạng")
      elif r==34:
         print("=>",ngude[2],": an mạng, phú quý")
      elif r==16 or r==17:
         print("=>",ngude[3],": cô bần")
      elif r==24 or r==25 or r==54 or r==55:
         print("=>",ngude[3],": phú quý")
      elif r==32 or r==33:
         print("=>",ngude[3],": trường mạng")
      elif r==46 or r==47:
         print("=>",ngude[3],": vất vả")
      elif r==2 or r==3:
         print("=>",ngude[3],": quan lộc")
      elif r==6 or r==7 or r==14 or r==15 or r==36 or r==37 or r==52:
         print("=>",ngude[4],": cô bần")
      elif r==28 or r==29 or r==59:
         print("=>",ngude[4],": phú quý")
      elif r==44 or r==45:
         print("=>",ngude[4],": vất vả")
   def saoHan1(self):
      print("10.1: XEM SAO, XEM HẠN")
      print("*Hăy nhập thông tin của bạn!")
      while True:
         try:
            a=int(input("*Số tuổi của bạn: "))
            sex=int(input("*Giới tính của bạn (Nam/Nữ: 1/0): "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      print("-"*20)
      if a<10 or a>99 or sex>1 or sex<0:
         mbox.showwarning("Thông báo",e+"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 10 đến 99)")
      else:
         if (sex==1 and a in sao1) or (sex==0 and a in sao6):
            print("- La Hầu: sao xấu, chủ mồm miệng, cửa quan, tai mắt, máu huyết sản nạn, buồn rầu")
         elif (sex==1 and a in sao2) or (sex==0 and a in sao5):
            print("- Thổ Tú: sao trung bình, chủ tiểu nhân, xuất hành không thuận, nhà cửa không vui, chăn nuôi thua lỗ")
         elif (sex==1 and a in sao3) or (sex==0 and a in sao9):
            print("- Thủy Diệu: sao trung bình, chủ Tài, Lộc, Hỷ; chủ phòng việc đi sông nước và điều ăn tiếng nói")
         elif (sex==1 and a in sao4) or (sex==0 and a in sao8):
            print("- Thái Bạch: sao xấu, hao tán tiền của, tiểu nhân, kiện tụng, bệnh nội tạng")
         elif (sex==1 and a in sao5) or (sex==0 and a in sao7):
            print("- Thái Dương: sao tốt, chủ hưng vượng tài lộc")
         elif (sex==1 and a in sao6) or (sex==0 and a in sao2):
            print("- Vân Hán: sao trung bình, chủ sự thủ cựu; phòng thương tật, ốm đau, sản nạn, nóng nảy, mồm miệng, kiện tụng, giấy tờ")
         elif (sex==1 and a in sao7) or (sex==0 and a in sao1):
            print("- Kế Đô: sao xấu, chủ hung dữ, ám muội, thị phi, buồn rầu")
         elif (sex==1 and a in sao8) or (sex==0 and a in sao4):
            print("- Thái Âm: sao tốt, chủ sự toại nguyện về danh lợi; riêng nữ phòng ốm đau, tật ách, sản nạn")
         else:
            print("- Mộc Đức: sao tốt, chủ hướng tới sự an vui hoà hợp")
         if (sex==1 and a in han1) or (sex==0 and a in han3):
            print("- Tam Kheo: đau mắt, đề phòng tai nạn chân tay")
         elif a in han2:
            print("- Ngũ Hộ: hao tài")
         elif (sex==1 and a in han3) or (sex==0 and a in han1):
            print("- Thiên Tinh: kiện tụng, lao tù")
         elif (sex==1 and a in han4) or (sex==0 and a in han8):
            print("- Toán Tận: gặp nạn bất ngờ")
         elif (sex==1 and a in han5) or (sex==0 and a in han7):
            print("- Thiên La: bệnh tật")
         elif a in han6:
            print("- Địa Võng: nhiều chuyện buồn, thị phi")
         elif (sex==1 and a in han7) or (sex==0 and a in han5):
            print("- Diêm Vương: không tốt đối với phụ nữ, nhất là khi sinh đẻ")
         else:
            print("- Huỳnh Tuyền: bệnh nặng nguy hiểm")
         print("*Lưu ý: Về phần hạn thì tất cả đều xấu. Tuy nhiên, nó còn phụ thuộc vào cung bát quái, mệnh ngũ hành của mỗi cá nhân.")
         print("=> Vậy nên bạn cũng đừng quá lo lắng nhé!")
      print("-"*50)

   def saoHan2(self):
      print("10.2: CÁCH TIỄN SAO XẤU VÀ NGHÊNH SAO TỐT")
      print("*Hăy nhập thông tin của bạn!")
      while True:
         try:
            a=int(input("*Số tuổi của bạn: "))
            sex=int(input("*Giới tính của bạn (Nam/Nữ: 1/0): "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      print("-"*20)
      if a<10 or a>99 or sex>1 or sex<0:
         mbox.showerror("Lỗi",e+"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 10 đến 99)")
      else:
         if (sex==1 and a in sao1) or (sex==0 and a in sao6):
            print("=> La Hầu:")
            bv="Thiên Cung Thần Thủ La Hầu (giấy vàng)"
            k="Cung thỉnh: Thiên cung Thần Thủ La Hầu, Thần Thủ tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 8, từ 21 đến 23 giờ, thắp 9 ngọn đèn hướng Bắc làm lễ"
         elif (sex==1 and a in sao2) or (sex==0 and a in sao5):
            print("=> Thổ Tú:")
            bv="Trung ương Mậu Kỷ Thổ Đức tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Hoàng Trung Đại Thánh Thổ Địa, Địa La Thổ Tú tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 19, từ 19 đến 21 giờ, thắp 5 ngọn đèn hướng Tây làm lễ"
         elif (sex==1 and a in sao3) or (sex==0 and a in sao9):
            print("=> Thuỷ Diệu:")
            bv="Bắc phương Nhâm Quý Thuỷ Đức tinh quân (giấy đen)"
            k="Cung thỉnh: Thiên đình Thuỷ Đức Kim Nữ cung, Đại Thánh Nhâm Quý Thuỷ Diêm tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 21, từ 21 đến 23 giờ, thắp 7 ngọn đèn hướng Bắc làm lễ"
         elif (sex==1 and a in sao4) or (sex==0 and a in sao8):
            print("=> Thái Bạch:")
            bv="Tây phương Canh Tân Kim Đức Thái Bạch tinh quân (giấy trắng)"
            k="Cung thỉnh: Thiên đình Hạc Linh cung Đại Thánh Kim Đức Thái Bạch tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 15, từ 21 đến 23 giờ, thắp 8 ngọn đèn hướng Tây làm lễ"
         elif (sex==1 and a in sao5) or (sex==0 and a in sao7):
            print("=> Thái Dương:")
            bv="Nhật cung Thái Dương Thiên Tử tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Uất Ly cung Đại Thánh Đang Nguyên Hải, Nhật cung Thái Dương tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 27, từ 21 đến 23 giờ, thắp 12 ngọn đèn hướng chính Đông làm lễ"
         elif (sex==1 and a in sao6) or (sex==0 and a in sao2):
            print("=> Vân Hán:")
            bv="Nam phương Bính Đinh Hoả Đức tinh quân (giấy hồng)"
            k="Cung thỉnh: Thiên đình Minh Ly cung Đại Thánh Hoả Đức Vân Hán tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 15, từ 21 đến 23 giờ, thắp 8 ngọn đèn hướng Tây làm lễ"
         elif (sex==1 and a in sao7) or (sex==0 and a in sao1):
            print("=> Kế Đô:")
            bv="Thiên Cung Thần Vĩ Kế Đô tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Bảo Vĩ cung Đại Thánh, Thần Vĩ Kế Đô tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 18, từ 21 đến 23 giờ, thắp 21 ngọn đèn hướng Tây làm lễ"
         elif (sex==1 and a in sao8) or (sex==0 and a in sao4):
            print("=> Thái Âm:")
            bv="Nguyệt Cung Thái Âm Hoàng Hậu tinh quân (giấy vàng)"
            k="Cung thỉnh: Thiên đình Kết Lâu cung Đại Thánh, Tổ Diệu Nguyệt Phu Thái Âm tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 26, từ 19 đến 21 giờ, thắp 7 ngọn đèn hướng Tây làm lễ"
         else:
            print("=> Mộc Đức:")
            bv="Đông phương Giáp Ất Mộc Đức tinh quân (giấy xanh)"
            k="Cung thỉnh: Thiên đình Thánh Vân cung Đại Thánh Trùng Quan Triều Nguyên Mộc Đức tinh quân vị tiền"
            cc="Mỗi tháng cúng ngày 25, từ 19 đến 21 giờ, thắp 20 ngọn đèn hướng Đông làm lễ"
         print("- Bài vị:",bv,"\n- Khấn:\n",k,"\n- Cách cúng:",cc,"(cách bài trí các ngọn đèn xem tại mục 10.3)")
      print("-"*50)
   def saoHan3(self):
      print("10.3: CỬU DIỆU TINH (SƠ ĐỒ BÀY ĐÈN CÚNG SAO)")
      while True:
         try:
            a=int(input("*Số tuổi của bạn: "))
            sex=int(input("*Giới tính của bạn (Nam/Nữ: 1/0): "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      print("-"*20)
      if a<10 or a>99 or sex>1 or sex<0:
         mbox.showerror("Lỗi",e+"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 10 đến 99)")
      else:
         if (sex==1 and a in sao1) or (sex==0 and a in sao6):
            print("\t\t La  Hầu")
            print("\t\t *     *\n\t\t *     *\n\t\t       *\n\t\t    *  \n\t\t *    \n\t\t    *  \n\t\t       *")
         elif (sex==1 and a in sao2) or (sex==0 and a in sao5):
            print("\t\t Thổ Tú")
            print("\t\t   *  \n\t\t * * *\n\t\t   *  ")
         elif (sex==1 and a in sao3) or (sex==0 and a in sao9):
            print("\t\tThuỷ Diệu")
            print("\t\t    *  \n\t\t  *   *\n\t\t    *  \n\t\t  *   *\n\t\t    *  ")
         elif (sex==1 and a in sao4) or (sex==0 and a in sao8):
            print("\t\t  Thái Bạch")
            print("\t\t    *  *\n\t\t    *  *\n\t\t    *  *\n\t\t    *  *\n\t\t")
         elif (sex==1 and a in sao5) or (sex==0 and a in sao7):
            print("\t\tThái Dương")
            print("\t\t * * * *\n\t\t * * * *\n\t\t *     *\n\t\t *     *")
         elif (sex==1 and a in sao6) or (sex==0 and a in sao2):
            print("\t\tVân Hán")
            print("\t\t * * *\n\t\t *\n\t\t * * *\n\t\t * * *\n\t\t * * *\n\t\t   * *")
         elif (sex==1 and a in sao7) or (sex==0 and a in sao1):
            print("\t\t  Kế Đô")
            print("\t\t    *\n\t\t* *   * *\n\t\t* *   * *\n\t\t* *   * *\n\t\t* *   * *\n\t\t  *   *\n\t\t  *   *")
         elif (sex==1 and a in sao8) or (sex==0 and a in sao4):
            print("\t\t Thái Âm")
            print("\t\t  *   *\n\t\t  *   *\n\t\t    *\n\t\t  *\n\t\t    *")
         elif (sex==1 and a in sao9) or (sex==0 and a in sao3):
            print("\t\t Mộc Đức")
            print("\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *\n\t\t    *\n\t\t       *\n\t\t    *\n\t\t *")
         else:
            mbox.showerror("Lỗi",e)
      print("-"*50)
   def hungTai(self):
      print("11: HUNG NIÊN, TAM TAI")
      print("*Giải thích: Hung niên, tam tai là gì?")
      print("- Hung niên, tam tai là những năm rơi vào sao chiếu mệnh không có lợi, đặc biệt về việc hôn nhân, cưới gả và cất nhà, xây dựng nhà cửa.")
      print("- Hung niên: chớ lập gia đình, thận trọng trong việc giao dịch kinh doanh. Tiến hành cất nhà ở tuổi này cũng được nhưng không tốt lắm.")
      print("- Tam tai: kỵ cất nhà và cưới gả (năm tam tai thường là của tuổi con trai, tuổi con gái thì không sao vì phần làm nhà là phần của người nam.")
      print("*Bây giờ, hăy nhập thông tin của bạn!")
      print("-"*20)
      from tkinter import messagebox
      window = Tk() 
      window.title("Hung niên, tam tai") 
      window.geometry('500x200+200+200')
      lbl=Label(window, text="Địa chi (con giáp) của bạn:") 
      lbl.grid(column=0, row=0)      
      gt=Combobox(window) 
      gt['values']=chi
      gt.grid(column=1, row=0)
      def clicked():
         lbl = Label(window, text="Kết quả:")
         lbl.grid(column=0, row=2)
         lbl = Label(window, text=" ")
         lbl.grid(column=0, row=1)
         txt = scrolledtext.ScrolledText(window,width=30,height=5)
         txt.grid(column=1, row=2)
         if gt.current()==0:
            txt.insert(INSERT,"- Tuổi hung niên: Măo\n- Năm tam tai: Dần, Măo, Thìn")
         elif gt.current()==1:
            txt.insert(INSERT,"- Tuổi hung niên: Sửu\n- Năm tam tai: Hợi, Tý, Sửu")
         elif gt.current()==2:
            txt.insert(INSERT,"- Tuổi hung niên: Thân\n- Năm tam tai: Thân, Dậu, Tuất")
         elif gt.current()==3:
            txt.insert(INSERT,"- Tuổi hung niên: Dậu\n- Năm tam tai: Tỵ, Ngọ, Mùi")         
         elif gt.current()==4:
            txt.insert(INSERT,"- Tuổi hung niên: Thìn\n- Năm tam tai: Dần, Măo, Thìn")
         elif gt.current()==5:
            txt.insert(INSERT,"- Tuổi hung niên: Hợi\n- Năm tam tai: Hợi, Tý, Sửu")
         elif gt.current()==6:
            txt.insert(INSERT,"- Tuổi hung niên: Dậu\n- Năm tam tai: Thân, Dậu, Tuất")
         elif gt.current()==7:
            txt.insert(INSERT,"- Tuổi hung niên: Tuất\n- Năm tam tai: Tỵ, Ngọ, Mùi")                  
         elif gt.current()==8:
            txt.insert(INSERT,"- Tuổi hung niên: Dần\n- Năm tam tai: Dần, Măo, Thìn")
         elif gt.current()==9:
            txt.insert(INSERT,"- Tuổi hung niên: Tý\n- Năm tam tai: Hợi, Tý, Sửu")
         elif gt.current()==10:
            txt.insert(INSERT,"- Tuổi hung niên: Tuất\n- Năm tam tai: Thân, Dậu, Tuất")
         elif gt.current()==11:
            txt.insert(INSERT,"- Tuổi hung niên: Hợi\n- Năm tam tai: Tỵ, Ngọ, Mùi")
      btn = Button(window, text="Xác nhận", command=clicked) 
      btn.grid(column=2, row=0)
      window.mainloop()
   def vanMenh1(self):
      while True:
         try:
            y=int(input(iny))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
         finally:
            print("-"*20)
      if y<0:
         mbox.showerror("Lỗi",e)
      else:
         r=y%60
         if r==0 or r==31:
            print("- Số may mắn là: 1, 3, 6, 8\n- Hợp màu: đen, xanh\n- Kỵ màu: vàng, đỏ, trắng")
         elif r==1 or r==9 or r==38 or r==39 or r==53:
            print("- Số may mắn là: 1, 6\n- Hợp màu: đen, xanh\n- Kỵ màu: vàng, đỏ, trắng")
         elif r==2 or r==3 or r==25 or r==32 or r==33:
            print("- Số may mắn là: 4, 9\n- Hợp màu: trắng, đen, xanh\n- Kỵ màu: vàng, đỏ")
         elif r==4:
            print()
   def hoangHac1(self):
      print("13.1: NGÀY HOÀNG ĐẠO, NGÀY HẮC ĐẠO")
      print("*Khái niệm: Trong một tháng đều có 4 ngày Hoàng đạo và 4 ngày Hắc đạo")
      print("- Ngày Hoàng đạo: tốt, có thể cưới gả, chôn cất, đám tang, cải táng, làm nhà, mở cửa hàng, cửa hiệu, đi xa...")
      print("- Ngày Hắc đạo: không nên làm việc lớn, tối kỵ việc cưới gả, an táng, làm nhà, làm bếp...")
      print("-"*20)
      m=int(input("*Nhập tháng âm lịch: "))
      if m<1 or m>12:
         mbox.showerror("Lỗi",e)
      else:
         hd1="- Ngày Hoàng đạo là: "
         hd2="- Ngày Hắc đạo là: "
         if m==1 or m==7:
            print(hd1,chi[1],chi[2],chi[6],chi[8])
            print(hd2,chi[7],chi[4],chi[0],chi[10])
         elif m==2 or m==8:
            print(hd1,chi[3],chi[4],chi[10],chi[1])
            print(hd2,chi[9],chi[6],chi[0],chi[2])
         elif m==3 or m==9:
            print(hd1,chi[5],chi[6],chi[10],chi[0])
            print(hd2,chi[11],chi[8],chi[4],chi[2])
         elif m==4 or m==10:
            print(hd1,chi[7],chi[8],chi[0],chi[2])
            print(hd2,chi[1],chi[10],chi[4],chi[6])
         elif m==5 or m==11:
            print(hd1,chi[9],chi[10],chi[2],chi[4])
            print(hd2,chi[3],chi[0],chi[8],chi[6])
         else:
            print(hd1,chi[11],chi[0],chi[4],chi[6])
            print(hd2,chi[5],chi[2],chi[8],chi[10])
      print("-"*50)
   def hoangHac2(self):
      from tkinter import messagebox
      window = Tk() 
      window.title("Tra giờ hoàng đạo") 
      window.geometry('400x100+200+200')
      lbl = Label(window, text="Ngày âm lịch:") 
      lbl.grid(column=0, row=0)      
      gt = Combobox(window) 
      gt['values']=chi
      gt.grid(column=1, row=0)
      def clicked():
         if gt.current()==0 or gt.current()==6:
            mbox.showinfo(kq,"Giờ hoàng đạo là: Tý, Sửu, Măo, Ngọ, Thân, Dậu")
         elif gt.current()==1 or gt.current==7:
            mbox.showinfo(kq,"Giờ hoàng đạo là: Dần, Măo, Tỵ, Thân, Tuất, Hợi")
         elif gt.current()==2 or gt.current==8:
            mbox.showinfo(kq,"Giờ hoàng đạo là: Tý, Sửu, Thin, Tỵ, Mùi, Tuất")
         elif gt.current()==3 or gt.current==9:
            mbox.showinfo(kq,"Giờ hoàng đạo là: Tý, Dần, Măo, Ngọ, Mùi, Dậu")
         elif gt.current()==4 or gt.current==10:
            mbox.showinfo(kq,"Giờ hoàng đạo là: Dần, Thin, Tỵ, Thân, Dậu, Hợi")
         elif gt.current()==5 or gt.current==11:
            mbox.showinfo(kq,"Giờ hoàng đạo là: Tý, Sửu, Thin, Tỵ, Mùi, Tuất")
         else:
            mbox.showerror("Lỗi",e)
      btn = Button(window, text="Xác nhận", command=clicked) 
      btn.grid(column=2, row=0)
      window.mainloop()
   def xayDung1(self):
      print("14.1: XEM TUỔI XÂY NHÀ")
      print("*Khái niệm: Làm nhà là một việc hệ trọng nên cần phải tính toán xem xét thật kỹ lưỡng từng phần như (chữ in hoa là sao tốt, chữ in thường là sao xấu):")
      print("- Cửu trạch: ",cuutrach)
      print("- Hạn cửu diệu: ",cuudieu,"(chi tiết xem phần 10.1)")
      print("- Hoang ốc: ",hoangoc)
      print("- Kim lâu: ",kimlau)
      print("- Tam tai: là ba năm liên tiếp xảy ra bệnh tật, ốm đau, tai nạn, mất mát tài sản, tiền của, kiện tụng... (chi tiết xem phần 11)")
      tx=['Bốn tốt:','Ba tốt một xấu:','Hai tốt hai xấu:','Ba xấu một tốt:']
      print("-"*20)
      while True:
         try:
            a=int(input("*Nhập số tuổi của bạn: "))
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
      if a<18 or a>99:
         mbox.showwarning("Thông báo",e+"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 18 đến 99)")
      else:
         if a in sao1:
            print("=>",tx[1],cuutrach[0],'-',cuudieu[0],'-',hoangoc[3],'-',kimlau[4])
         elif a in sao2:
            print("=>",tx[3],cuutrach[1],'-',cuudieu[1],'-',hoangoc[4],'-',kimlau[1])
         elif a==sao3[1] or a==sao3[2]:
            print("=>",tx[3],cuutrach[2],'-',cuudieu[2],'-',hoangoc[2],'-',kimlau[1])
         elif a in sao3 and a!=sao3[0] and a!=sao3[1] and a!=sao3[2]:
            print("=>",tx[2],cuutrach[2],'-',cuudieu[2],'-',hoangoc[5],'-',kimlau[4])
         elif a==sao4[1] or a==sao4[2] or a==sao4[3]:
            print("=>",tx[2],cuutrach[3],'-',cuudieu[3],'-',hoangoc[3],'-',kimlau[4])
         elif a in sao4 and a!=sao4[0] and a!=sao4[1] and a!=sao4[2] and a!=sao4[3]:
            print("=>",tx[3],cuutrach[3],'-',cuudieu[3],'-',hoangoc[0],'-',kimlau[2])
         elif a==sao5[1] or a==sao5[2] or a==sao5[3] or a==sao5[4]:
            print("=>",tx[2],cuutrach[4],'-',cuudieu[4],'-',hoangoc[3],'-',kimlau[2])
         elif a==sao5[5] or a==sao5[6] or a==sao5[7] or a==sao5[8]:
            print("=>",tx[1],cuutrach[4],'-',cuudieu[4],'-',hoangoc[1],'-',kimlau[4])
         elif a in sao6 and a!=sao4[6] and a!=sao4[7] and a!=sao4[8]:
            print("=>",tx[2],cuutrach[5],'-',cuudieu[5],'-',hoangoc[5],'-',kimlau[4])
         elif a==sao6[6] or a==sao4[7] or a==sao4[8]:
            print("=>",tx[4],cuutrach[5],'-',cuudieu[5],'-',hoangoc[2],'-',kimlau[3])
         elif a in sao7 and a!=sao7[0] and a!=sao7[8] and a!=sao7[9]:
            print("=>",tx[3],cuutrach[6],'-',cuudieu[6],'-',hoangoc[0],'-',kimlau[3])
         elif a in sao8 and a!=sao8[0] and a!=sao8[8] and a!=sao8[9]:
            print("=>",tx[0],cuutrach[7],'-',cuudieu[7],'-',hoangoc[1],'-',kimlau[4])
         elif a in sao9:
            print("=>",tx[2],cuutrach[8],'-',cuudieu[8],'-',hoangoc[2],'-',kimlau[0])
      print("*Đặc biệt: Nếu như tuổi bạn năm nay rơi vào hạn tam tai thì không nên xây dựng và tu sửa nhà cửa (xem hạn tam tai ở phần 11)")
      print("-"*50)
   def xayDung2(self):
      print("14.2: HƯỚNG NHÀ")
      print("*Khái niệm: Trong xây dựng, tu tạo nhà cửa, ngoài những điều cần tránh, thì hướng nhà cũng rất quan trọng.\
Nếu tránh được những điều xấu cần tránh mà hướng nhà vào hướng xấu so với tuổi chủ nhà thì cũng rất nguy hiểm")
      ht="- Các hướng tốt (xếp theo thứ tự tốt giảm dần):"
      hx="- Các hướng khác đều xấu, xấu nhất là hướng:"
      while True:
         try:
            y=int(input(iny))
            s=input(ins)
            break
         except ValueError:
            mbox.showerror("Lỗi",e)
         finally:
            print("-"*20)
      if y<0:
         mbox.showerror("Lỗi",e)
      else:
         r=y%60
         if (r in huong1m and s=='') or (r in huong1f and s==' '):
            print(ht,"\n +",huong[2],"\n +",huong[0],"\n +",huong[7],"\n +",huong[6]); print(hx,huong[4])
         elif (r in huong2m and s=='') or (r in huong2f and s==' '):
            print(ht,"\n +",huong[4],"\n +",huong[5],"\n +",huong[3],"\n +",huong[1]); print(hx,huong[2])
         elif (r in huong3 and s=='') or (r in huong4 and s==' '):
            print(ht,"\n +",huong[5],"\n +",huong[4],"\n +",huong[1],"\n +",huong[3]); print(hx,huong[0])
         elif (r in huong5m and s=='') or (r in huong5f and s==' '):
            print(ht,"\n +",huong[3],"\n +",huong[1],"\n +",huong[4],"\n +",huong[5]); print(hx,huong[7])
         elif (r in huong6m and s=='') or (r in huong6f and s==' '):
            print(ht,"\n +",huong[1],"\n +",huong[3],"\n +",huong[5],"\n +",huong[4]); print(hx,huong[6])
         elif (r in huong7m and s=='') or (r in huong7f and s==' '):
            print(ht,"\n +",huong[7],"\n +",huong[6],"\n +",huong[2],"\n +",huong[0]); print(hx,huong[3])
         elif (r in huong4 and s=='') or (r in huong3 and s==' '):
            print(ht,"\n +",huong[6],"\n +",huong[7],"\n +",huong[0],"\n +",huong[2]); print(hx,huong[1])
         elif r in huong8:
            print(ht,"\n +",huong[0],"\n +",huong[2],"\n +",huong[6],"\n +",huong[7]); print(hx,huong[5])
         else:
            mbox.showwarning("Thông báo",f)
      print("-"*50)
   def onWidget(self):
      mbox.showerror("Lỗi",e)
   def onWarn(self):
      mbox.showwarning("Thông báo", "Tính năng sắp ra mắt!\nXin vui lòng trở lại sau.")
   def onQuit(self):
      mbox.askquestion("Xác nhận", "Bạn chắc chắn muốn thoát không?")
   def onGame(self):
      mbox.showinfo("Thông tin", "Xin chúc mừng")
class Application(tk.Frame):
   def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
   def onQuit(self):
        mbox.askokcancel("Xác nhận", "Bạn chắc chắn muốn thoát không?")
   def create_widgets(self):
        self.choice = tk.Button(self, text="Tuỳ chọn", fg="blue", command=self)
        self.choice.pack(side="left", padx=5, pady=5)
        self.quit = tk.Button(self, text="Thoát", fg="red", command=self.master.destroy)
        self.quit.pack(side="right", padx=5, pady=5)
        closeButton = Button(self, text="Trở lại")
        closeButton.pack(side="right", padx=5, pady=5)
        okButton = Button(self, text="Xác nhận")
        okButton.pack(side="right")
        
window = Tk()
ex = boi(window)
app = Application(master=window)
window.geometry("450x400+800+150")
window.mainloop()
