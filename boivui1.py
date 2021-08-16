##Phần giới thiệu app:
print("***PHẦN MỀM BÓI VUI 2019!***".center(50,' '))
print("Phiên bản: v1.0".center(50,' '))
print("="*50)
print("*Đây là các chức năng trong ứng dụng: ")
print("1: Hôn nhân")
print("2: Bát quái")
print("3: Ngũ hành")
print("4: Thiên can")
print("5: Địa chi")
print("6: Dương lịch")
print("7: Âm lịch")
print("8: Ngày hoàng đạo, ngày hắc đạo")
print("9: Hung niên, tam tai")
print("10: Sao tốt, sao xấu")
print("11: Coi sao, coi hạn")
print("12: Sự tương quan giữa 12 con giáp")
print("13: Ngũ Đế")
e="=> Lỗi nhập dữ liệu. Vui lòng nhập lại!"
while True:
    try:
        select=int(input("*Vui lòng chọn phần mà bạn muốn xem: "))
        break
    except ValueError:
        print(e)
    finally:
        print("*Chào mừng bạn sử dụng ứng dụng!")
print("-"*40)
##Định nghĩa:
can=['Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm']
can0=['Quý','Quy','quy','quý','qui','quí','Quí','Qui']
can1=['Giáp','Giap','giap','giáp']
can2=['Ất','At','at','ất']
can3=['Bính','Binh','binh','bính']
can4=['Đinh','Dinh','đinh','dinh']
can5=['Mậu','Mau','mau','mậu']
can6=['Kỷ','Ky','ky','kỷ','kỉ','ki','Kỉ','Ki']
can7=['Canh','canh']
can8=['Tân','Tan','tan','tân']
can9=['Nhâm','Nham','nham','nhâm']
chi=['Hợi','Tý','Sửu','Dần','Măo','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất']
chi0=['Hợi','Hoi','hoi','hợi']
chi1=['Tý','tí','tý','ti','Ti','Tí']
chi2=['Sửu','Suu','suu','sửu']
chi3=['Dần','Dan','dan','dần']
chi4=['Măo','Mao','mao','măo','Mẹo','Meo','meo','mẹo']
chi5=['Thìn','Thin','thin','thìn']
chi6=['Tỵ','Ty','ty','tỵ']
chi7=['Ngọ','Ngo','ngo','ngọ']
chi8=['Mùi','Mui','mui','mùi']
chi9=['Thân','Than','than','thân']
chi10=['Dậu','Dau','dau','dậu']
chi11=['Tuất','Tuat','tuat','tuất']
bq=['Càn','Khảm','Cấn','Chấn','Tốn','Ly','Khôn','Đoài']
bq1=['Càn','càn']
bq2=['Khảm','Kham','kham','khảm']
bq3=['Cấn','cấn']
bq4=['Chấn','Chan','chan','chấn']
bq5=['Tốn','Ton','ton','tốn']
bq6=['Ly','ly','li','Li']
bq7=['Khôn','Khon','khon','khôn']
bq8=['Đoài','Doai','doai','đoài']
bqhh=['Sinh khí','Phước đức','Thiên y','Phục vị','Tuyệt mệnh','Hoạ hại','Ngũ quỷ','Lục sát']
ad="- Âm dương:"
nh="- Ngũ hành:"
##Input:
if select==10 or select==13 or select==12:
        print("Tính năng sắp ra mắt!\nXin vui lòng trở lại sau.")
elif select>13 or select<1:
        print(e)    

##Hôn nhân:
if select==1:
    print("1: HÔN NHÂN")
    print("a) Bát quái hợp hôn\nb) Bát san giao chiến\nc) Bát san tuyệt mệnh\nd) Thiên can hợp hôn\ne) Địa chi hợp hôn\nf) Ngày tốt, xấu cho hôn nhân (mục này chỉ dành cho bên nhà gái)\ng) Tự kiểm tra việc hôn nhân")
    select1=input("Chọn phần cần xem (a-g): ")
    print("-"*40)
    if select1=='a' or select1=='A':
        print("a) BÁT QUÁI HỢP HÔN:")
        print("*Khái niệm: Sự phối hợp của các cung kí sinh (Bát quái) Càn, Khôn, Chấn... gọi là Bát quái hợp hôn sẽ cho ra kết quả cuộc hôn nhân như dưới đây:")
        print("-"*20)
        m=input("*Nhập cung bát quái của nam: ")
        f=input("*Nhập cung bát quái của nữ: ")
        if (m in bq1 and f in bq8) or (m in bq2 and f in bq5) or (m in bq3 and f in bq7) or (m in bq4 and f in bq6) or (m in bq5 and f in bq2) or (m in bq6 and f in bq4) or (m in bq7 and f in bq3) or (m in bq8 and f in bq1):
            print("=> Sinh khí: rất tốt")
        elif (m in bq1 and f in bq7) or (m in bq2 and f in bq6) or (m in bq3 and f in bq8) or (m in bq4 and f in bq5) or (m in bq5 and f in bq4) or (m in bq6 and f in bq2) or (m in bq7 and f in bq1) or (m in bq8 and f in bq3):
            print("=> Phước đức: tốt, tuy có xung khắc")
        elif (m in bq1 and f in bq3) or (m in bq2 and f in bq4) or (m in bq3 and f in bq1) or (m in bq4 and f in bq2) or (m in bq5 and f in bq5) or (m in bq6 and f in bq5) or (m in bq7 and f in bq8) or (m in bq8 and f in bq7):
            print("=> Thiên y: mệnh vợ làm chủ tiền tài")    
        elif (m in bq1 and f in bq1) or (m in bq2 and f in bq2) or (m in bq3 and f in bq3) or (m in bq4 and f in bq4) or (m in bq5 and f in bq6) or (m in bq6 and f in bq6) or (m in bq7 and f in bq7) or (m in bq8 and f in bq8):
            print("=> Phục vị: đôi khi dễ xảy ra việc khắc khẩu, con cháu thành đạt trung bình")
        elif (m in bq1 and f in bq6) or (m in bq2 and f in bq7) or (m in bq3 and f in bq5) or (m in bq4 and f in bq8) or (m in bq5 and f in bq3) or (m in bq6 and f in bq1) or (m in bq7 and f in bq2) or (m in bq8 and f in bq4):
            print("=> Tuyệt mệnh: chồng chết sớm hoặc vợ bệnh nặng lúc hậu sản")
        elif (m in bq1 and f in bq5) or (m in bq2 and f in bq8) or (m in bq3 and f in bq6) or (m in bq4 and f in bq7) or (m in bq5 and f in bq1) or (m in bq6 and f in bq3) or (m in bq7 and f in bq4) or (m in bq8 and f in bq2):
            print("=> Hoạ hại: khắc khẩu bất hoà")
        elif (m in bq1 and f in bq4) or (m in bq2 and f in bq3) or (m in bq3 and f in bq2) or (m in bq4 and f in bq1) or (m in bq5 and f in bq7) or (m in bq6 and f in bq8) or (m in bq7 and f in bq5) or (m in bq8 and f in bq6):
            print("=> Ngũ quỷ: dễ sinh ly tử biệt")
        elif (m in bq1 and f in bq2) or (m in bq2 and f in bq1) or (m in bq3 and f in bq4) or (m in bq4 and f in bq3) or (m in bq5 and f in bq8) or (m in bq6 and f in bq7) or (m in bq7 and f in bq6) or (m in bq8 and f in bq5):
            print("=> Lục sát: chăn nuôi không đạt")
        else:
            print(e)
    elif select1=='b' or select1=='B':
        print("b) BÁT SAN GIAO CHIẾN:")
        print("*Khái niệm: là sự khắc khẩu bất hoà, xung đột triền miên, khi các cung Bát quái phối hợp với nhau.")
        print("-"*20)
        while True:
            try:
                y=int(input("*Nhập năm sinh của bạn: "))
                break
            except ValueError:
                print(e)    
        x=y%10
        z=y%12
        if (x==y==1) or (x==y==7) or (x==3 and z==11) or (x==8 and z==4) or (x==0 and z==4) or (x==4 and z==2) or (x==6 and z==10):
            print(bq[0],"><",bq[4],"\t",bq[0],"><",bq[6])
        elif (x==y==0) or (x==9 and z==7) or (x==4 and z==0) or (x==3 and z==9) or (x==6 and z==0) or (x==1 and z==4) or (x==7 and z==9) or (x==2 and z==0) or (x==9 and z==7):
            print(bq[6],"><",bq[2],"\t",bq[6],"><",bq[3],"\t",bq[6],"><",bq[5])
        elif (x==z==4) or (x==0 and z==8) or (x==5 and z==1) or (x==7 and z==1) or (x==2 and z==4) or (x==8 and z==10) or (x==3 and z==1):
            print(bq[3],"><",bq[4],"\t",bq[3],"><",bq[6])
        elif (x==z==5) or (x==1 and z==9) or (x==6 and z==2) or (x==8 and z==2) or (x==3 and z==5) or (x==9 and z==11):
            print(bq[4],"><",bq[0],"\t",bq[4],"><",bq[3])
        elif (x==z==6) or (x==8 and z==6) or (x==2 and z==8) or (x==5 and z==11) or (x==4 and z==8) or (x==0 and z==2) or (x==6 and z==8) or (x==1 and z==11):
            print(bq[1],"><",bq[4])
        elif (x==7 and z==5) or (x==2 and z==10) or (x==1 and z==7) or (x==4 and z==10) or (x==3 and z==7) or (x==9 and z==1) or (x==5 and z==7) or (x==0 and z==10):
            print(bq[5],"><",bq[0],"\t",bq[5],"><",bq[3])
        elif (x==y==3) or (x==z==9) or (x==6 and z==4) or (x==7 and z==3) or (x==0 and z==6) or (x==9 and z==3) or (x==2 and z==6) or (x==8 and z==0) or (x==4 and z==6):
            print(bq[2],"><",bq[6])
        else:
            print(bq[7],"><",bq[5])
    elif select1=='c' or select1=='C':
        print("c) BÁT SAN TUYỆT MỆNH:")
        print("*Khái niệm: là những cặp xấu nhất, mệnh người này triệt người kia, nhưng tất cả không có nghĩa là một trong hai sẽ tử biệt. Tuỳ theo mức xung khắc, nếu nhẹ thì dẫn đến khắc khẩu bất hoà, nặng thì con cái bệnh tật, hư hỏng và là nguyên nhân dẫn đến sự nghèo túng cơ cực.")
        print("-"*20)
        s=input("Nhập cung bát quái của bạn: ")
        if s in bq1:
            print("=>",bq[0].upper(),"><",bq[5].upper())
        elif s in bq2:
            print("=>",bq[1].upper(),"><",bq[6].upper())
        elif s in bq3:
            print("=>",bq[2].upper(),"><",bq[4].upper())
        elif s in bq4:
            print("=>",bq[3].upper(),"><",bq[7].upper())
            print("*Chú ý: đây là cặp xấu nhất, tuy nhiên nếu các can chi mệnh phù hợp thì độ nguy hại giảm thiểu rõ rệt.\nNhưng cũng đừng vì sự tương khắc ấy mà những người yêu nhau quá sợ hăi!")
        elif s in bq5:
            print("=>",bq[4].upper(),"><",bq[2].upper())
        elif s in bq6:
            print("=>",bq[5].upper(),"><",bq[0].upper())
        elif s in bq7:
            print("=>",bq[6].upper(),"><",bq[1].upper())
        elif s in bq8:
            print("=>",bq[7].upper(),"><",bq[3].upper())
            print("*Chú ý: đây là cặp xấu nhất, tuy nhiên nếu các can chi mệnh phù hợp thì độ nguy hại giảm thiểu rõ rệt.\nNhưng cũng đừng vì sự tương khắc ấy mà những người yêu nhau quá sợ hăi!")
        else:
            print(e)
    elif select1=='d' or select1=='D':
        print("d) THIÊN CAN HỢP HÔN:")
        while True:
            try:
                tc=input("*Nhập thiên can của bạn (ví dụ: Giáp, Ất,...): ")
                break
            except ValueError:
                print(e)  
        if tc in can1:
            print("+ Hợp:",can[6],"\n+ Phá:",can[5],"\n+ Xung:",can[7])
        elif tc in can2:
            print("+ Hợp:",can[7],"\n+ Phá:",can[6],"\n+ Xung:",can[8])
        elif tc in can3:
            print("+ Hợp:",can[8],"\n+ Phá:",can[7],"\n+ Xung:",can[9])
        elif tc in can4:
            print("+ Hợp:",can[9],"\n+ Phá:",can[8],"\n+ Xung:",can[0])
        elif tc in can5:
            print("+ Hợp:",can[0],"\n+ Phá:",can[9],"\n+ Xung:",can[1])
        elif tc in can6:
            print("+ Hợp:",can[1],"\n+ Phá:",can[0],"\n+ Xung:",can[2])
        elif tc in can7:
            print("+ Hợp:",can[2],"\n+ Phá:",can[1],"\n+ Xung:",can[3])
        elif tc in can8:
            print("+ Hợp:",can[3],"\n+ Phá:",can[2],"\n+ Xung:",can[4])
        elif tc in can9:
            print("+ Hợp:",can[4],"\n+ Phá:",can[3],"\n+ Xung:",can[5])
        elif tc in can0:
            print("+ Hợp:",can[5],"\n+ Phá:",can[4],"\n+ Xung:",can[6])
        else:
            print(e)
    elif select1=='e' or select1=='E':
        print("e) ĐỊA CHI HỢP HÔN:")
        while True:
            try:
                dc=input("*Nhập địa chi của bạn (hay còn gọi là con giáp): ")
                break
            except ValueError:
                print(e)  
        if dc in chi0 or dc in chi3:
            print("=>",chi[3],"hợp",chi[0])
        elif dc in chi1 or dc in chi2:
            print("=>",chi[1],"hợp",chi[2])
        elif dc in chi4 or dc in chi11:
            print("=>",chi[4],"hợp",chi[11])
        elif dc in chi5 or dc in chi10:
            print("=>",chi[5],"hợp",chi[10])
        elif dc in chi6 or dc in chi9:
            print("=>",chi[6],"hợp",chi[9])
        elif dc in chi7 or dc in chi8:
            print("=>",chi[7],"hợp",chi[8])
        else:
            print(e)
    elif select1=='f' or select1=='F':
        print("f) NGÀY TỐT, XẤU TRONG HÔN NHÂN (mục này chỉ dành cho bên nhà gái):")
        print("*Chú thích:\n- Đại lợi: tốt cho con gái xuất giá\n- Phòng Phu chủ: kỵ với chồng\n- Phòng Thê chủ: kỵ với bản thân\n- Phòng Công cô: kỵ với cha mẹ chồng\n- Phòng Nữ phụ mẫu: kỵ với cha mẹ ruột")
        print("+ Nếu trai gái mồ côi thì không sợ tháng kỵ phòng Công cô, phòng Nữ phụ mẫu.\n+ Tiểu lợi: kỵ với bà Mai (còn gọi là phòng Mai nhân), nếu không có bà Mai hay chỉ mượn làm giúp lễ cho đủ thì không ngại gì.")
        print("-"*20)
        x=input("*Nhập tuổi (con giáp) người nữ kết hôn: ")
        dl=" - Đại lợi:"; tl="- Tiểu lợi:"; pcc="- Phòng Công cô:"; ppm="- Phòng Nữ phụ mẫu:"; ppc="- Phòng Phu chủ:"; ptc="- Phòng Thê chủ:"
        t1="1, 7\n"; t2="2, 8\n"; t3="3, 9\n"; t4="4, 10\n"; t5="5, 11\n"; t6="6, 12\n"
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
            print(e)
##Bát quái
if select==2:
    print("2: BÁT QUÁI")
    print("a) Tra bát quái theo năm sinh\nb) Tra bát quái theo năm can chi")
    select2=input("Nhập mục mà bạn muốn xem (a-b): ")   
    print("-"*40)
    if select2=='a' or select2=='A':
        print("a) BÁT QUÁI THEO NĂM SINH:")
        print("*Giới thiệu: Có trên có dưới, có tả có hữu, có trước có sau nên gọi là Vũ. Có xưa có nay, có quá khứ có tương lai nên gọi là Trụ. Trong Vũ trụ có ánh sáng, tối tăm, ngày đêm, mưa gió, sấm chớp, sông hồ, ao rạch... nên luận thành Bát Quái gồm có:\n",bq)
        print("-"*20)
        while True:
            try:
                y=int(input("*Nhập năm sinh của bạn: "))
                break
            except ValueError:
                print(e)    
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
        print("*Chú ý: đây là cung Bát quái (cung Ký sinh), loại cung về vận mệnh đặc điểm của từng người, vận hạn cứ theo đó mà định hình. Còn loại cung còn lại (cung Bát trạch) chỉ là cung liên quan đến điền thổ, đến chỗ ở, việc xây cất nhà cửa, có sự phân biệt giữa nam và nữ, không nên nhầm lẫn.")
    elif select2=='b' or select=='B':
        print("b) BÁT QUÁI THEO NĂM CAN CHI:")
        print("*Giới thiệu: Có trên có dưới, có tả có hữu, có trước có sau nên gọi là Vũ. Có xưa có nay, có quá khứ có tương lai nên gọi là Trụ. Trong Vũ trụ có ánh sáng, tối tăm, ngày đêm, mưa gió, sấm chớp, sông hồ, ao rạch... nên luận thành Bát Quái gồm có:\n",bq)
        print("-"*20)
        x=input("*Nhập thiên can của bạn: ")
        y=input("*Nhập địa chi của bạn: ")
        if (x in can0 and y in chi8) or (x in can5 and y in chi1) or (x in can7 and y in chi1) or (x in can3 and y in chi7) or (x in can8 and y in chi10) or (x in can4 and y in chi4) or (x in can1 and y in chi11):
            print("=>",bq[0].upper(),"\n- Hướng: Tây Bắc\n- Tượng trưng: Trời, mặt trời, ban ngày, ánh sáng, cha, phái nam\n- Thuộc: dương Kim")
        elif (x in can5 and y in chi3) or (x in can9 and y in chi5) or (x in can2 and y in chi8) or (x in can1 and y in chi5) or (x in can7 and y in chi11) or (x in can3 and y in chi5) or (x in can3 and y in chi5) or (x in can8 and y in chi8):
            print("=>",bq[1].upper(),"\n- Hướng: chính Bắc\n- Tượng trưng: nước, con trai thứ\n- Thuộc: dương Thuỷ")
        elif (x in can3 and y in chi1) or (x in can4 and y in chi0) or (x in can7 and y in chi3) or (x in can6 and y in chi0) or (x in can9 and y in chi5) or (x in can5 and y in chi9) or (x in can1 and y in chi5) or (x in can0 and y in chi0) or (x in can6 and y in chi6):
            print("=>",bq[2].upper(),"\n- Hướng: Đông Bắc\n- Tượng trưng: núi non, con trai út\n- Thuộc: dương Thổ")
        elif (x in can7 and y in chi5) or (x in can2 and y in chi10) or (x in can4 and y in chi10) or (x in can9 and y in chi1) or (x in can5 and y in chi7) or (x in can1 and y in chi1) or (x in can0 and y in chi10):
            print("=>",bq[3].upper(),"\n- Hướng: chính Đông\n- Tượng trưng: sấm sét, con trai trưởng\n- Thuộc: dương Mộc")
        elif (x in can8 and y in chi6) or (x in can3 and y in chi11) or (x in can5 and y in chi11) or (x in can0 and y in chi2) or (x in can6 and y in chi8) or (x in can2 and y in chi2):
            print("=>",bq[4].upper(),"\n- Hướng: Đông Nam\n- Tượng trưng: gió băo, con gái trưởng\n- Thuộc: âm Mộc")
        elif (x in can4 and y in chi2) or (x in can9 and y in chi7) or (x in can8 and y in chi4) or (x in can1 and y in chi7) or (x in can0 and y in chi4) or (x in can6 and y in chi10) or (x in can2 and y in chi4) or (x in can7 and y in chi7):
            print("=>",bq[5].upper(),"\n- Hướng: chính Nam\n- Tượng trưng: lửa, con gái thứ\n- Thuộc: âm Hoả")
        elif (x in can6 and y in chi4) or (x in can1 and y in chi9) or (x in can0 and y in chi6) or (x in can3 and y in chi9) or (x in can8 and y in chi0) or (x in can4 and y in chi6) or (x in can7 and y in chi9) or (x in can9 and y in chi9):
            print("=>",bq[6].upper(),"\n- Hướng: Tây Nam\n- Tượng trưng: Đất, mặt trăng, ban đêm, bóng tối, mẹ, phái nữ\n- Thuộc: âm Thổ")
        elif (x in can6 and y in chi2) or (x in can8 and y in chi2) or (x in can2 and y in chi6) or (x in can4 and y in chi8) or (x in can9 and y in chi11) or (x in can5 and y in chi5) or (x in can2 and y in chi0):
            print("=>",bq[7].upper(),"\n- Hướng: chính Tây\n- Tượng trưng: ao hồ, sông rạch, con gái út\n- Thuộc: âm Kim")
        print("-"*20)
        print("*Chú ý: đây là cung Bát quái (cung Ký sinh), loại cung về vận mệnh đặc điểm của từng người, vận hạn cứ theo đó mà định hình. Còn loại cung còn lại (cung Bát trạch) chỉ là cung liên quan đến điền thổ, đến chỗ ở, việc xây cất nhà cửa, có sự phân biệt giữa nam và nữ, không nên nhầm lẫn.")
        
##Ngũ hành
if select==3:
    print("3: NGŨ HÀNH")
    print("a) Tra cung mệnh theo năm sinh\nb) Sơ đồ ngũ hành\nc) Các nguyên tắc ngũ hành chế hoá")
    select3=input("*Chọn phần muốn xem (a-c): ")
    print("-"*40)
    if select3=='a' or select3=='A':
        print("a) TRA CUNG MỆNH THEO NĂM SINH")
        y=int(input("*Nhập năm sinh của bạn: "))
        x=y%10
        z=y%12
        if (x==y==0) or (x==y==1):
            print("Mộc: Thạch Lựu Mộc (cây thạch lựu)")
        elif (x==y==2) or (x==y==3):
            print("Thuỷ: Đại Hải Thuỷ (nước biển lớn)")
        elif x==z==4 or (x==9 and z==5):
            print("Kim: Hải Trung Kim (vàng trong biển)")
        elif x==y==6 or x==y==7:
            print("Hoả: Lư Trung Hoả (lửa trong lò)")
        elif x==y==8 or x==y==9:
            print("Mộc: Đại Lâm Mộc (cây rừng lớn)")
        elif (x==0 and z==10) or (x==1 and z==11):
            print("Thổ: Lộ Bàn Thổ (đất đường đi)")
        elif (x==2 and z==0) or (x==3 and z==1):
            print("Kim: Kiếm Phong Kim (mũi kiếm vàng)")
        elif (x==4 and z==2) or (x==5 and z==3):
            print("Hoả: Sơn Đầu Hoả (lửa đầu núi)")
        elif (x==6 and z==4) or (x==7 and z==5):
            print("Thuỷ: Giang Hạ Thuỷ (nước dưới sông)")
        elif (x==8 and z==6) or (x==9 and z==7):
            print("Thổ: Thành Đầu Thổ (đất trên thành)")
        elif (x==0 and z==8) or (x==1 and z==9):
            print("Kim: Bạch Lạp Kim (vàng nến trắng)")
        elif (x==2 and z==10) or (x==3 and z==11):
            print("Mộc: Dương Liễu Mộc (cây dương liễu)")
        elif (x==4 and z==0) or (x==5 and z==1):
            print("Thuỷ: Tuyền Trung Thuỷ (nước trong suối)")
        elif (x==6 and z==2) or (x==7 and z==3):
            print("Thổ: Ốc Thượng Thổ (đất trên nhà)")
        elif (x==8 and z==4) or (x==9 and z==5):
            print("Hoả: Tích Lịch Hoả (lửa sấm sét)")
        elif (x==0 and z==6) or (x==1 and z==7):
            print("Mộc: Tùng Bá Mộc (cây tùng bách)")
        elif (x==2 and z==8) or (x==3 and z==9):
            print("Thuỷ: Trường Lưu Thuỷ (nước chảy dài)")
        elif (x==4 and z==10) or (x==5 and z==11):
            print("Kim: Sa Trung Kim (vàng trong cát)")
        elif (x==6 and z==0) or (x==7 and z==1):
            print("Hoả: Sơn Hạ Hoả (lửa dưới núi)")
        elif (x==8 and z==2) or (x==9 and z==3):
            print("Mộc: Bình Địa Mộc (cây sát đất)")
        elif (x==0 and z==4) or (x==1 and z==5):
            print("Thổ: Bích Thượng Thổ (đất trên tường)")
        elif (x==2 and z==6) or (x==3 and z==7):
            print("Kim: Kim Bạch Kim (vàng trắng vàng)")
        elif (x==4 and z==8) or (x==5 and z==9):
            print("Hoả: Phúc Đăng Hoả (lửa che đèn)")
        elif (x==6 and z==10) or (x==7 and z==11):
            print("Thuỷ: Thiên Hà Thuỷ (nước sông trời)")
        elif (x==8 and z==0) or (x==9 and z==1):
            print("Thổ: Đại Trạch Thổ (đất nhà lớn)")
        elif (x==0 and z==2) or (x==1 and z==3):
            print("Kim: Thoa Xuyến Kim (vàng trang sức)")
        elif (x==2 and z==4) or (x==3 and z==5):
            print("Mộc: Tang Đố Mộc (cây dâu tằm)")
        elif (x==4 and z==6) or (x==5 and z==7):
            print("Thuỷ: Đại Khê Thuỷ (nước suối lớn)")
        elif (x==6 and z==8) or (x==7 and z==9):
            print("Thổ: Sa Trung Thổ (đất trong cát)")
        else:
            print("Hoả: Thiên Thượng Hoả (lửa trên trời)")
    if select3=='c' or select3=='C':
        print("c) CÁC NGUYÊN TẮC NGŨ HÀNH CHẾ HÓA:")
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
               
##Coi sao, coi hạn (Nam, Nữ):
if select==11:
    print("11: COI SAO, COI HẠN")
    print("a) Bảng coi sao, coi hạn\nb) Cách tiễn sao xấu và nghênh sao tốt\nc) Cửu diệu tinh (sơ đồ bày đèn cúng sao)")
    select11=input("*Chọn phần cần xem (a-c): ")
    print("-"*40)
    sao1=[10,19,28,37,46,55,64,73,82,91]
    sao2=[11,20,29,38,47,56,65,74,83,92]
    sao3=[12,21,30,39,48,57,66,75,84,93]
    sao4=[13,22,31,40,49,58,67,76,85,94]
    sao5=[14,23,32,41,50,59,68,77,86,95]
    sao6=[15,24,33,42,51,60,69,78,87,96]
    sao7=[16,25,34,43,52,61,70,79,88,97]
    sao8=[17,26,35,44,53,62,71,80,89,98]
    sao9=[18,27,36,45,54,63,72,81,90,99]
    han1=[11,19,20,28,37,46,55,64,73,82,91,99]
    han2=[12,21,29,30,38,47,56,65,74,83,92]
    han3=[13,22,31,39,40,48,57,66,75,84,93]
    han4=[14,23,32,41,49,50,58,67,76,85,94]
    han5=[15,24,33,42,51,59,60,68,77,86,95]
    han6=[16,25,34,43,52,61,69,70,78,87,96]
    han7=[17,26,35,44,53,62,71,79,80,88,97]
    han8=[10,18,27,36,45,54,63,72,81,89,90,98]
    if select11=='a' or select11=='A':
        print("a) BẢNG COI SAO, COI HẠN")
        print("*Hăy nhập thông tin của bạn!")
        while True:
            try:
                a=int(input("*Số tuổi của bạn: "))
                sex=int(input("*Giới tính của bạn (Nam/Nữ: 1/0): "))
                break
            except ValueError:
                print(e)
        print("-"*20)
        if a<10 or a>99 or sex>1 or sex<0:
            print(e,"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 10 đến 99)")
        else:
    #Bảng coi sao:
            if (sex==1 and a in sao1) or (sex==0 and a in sao6):
                print("- La Hầu: sao xấu, chủ mồm miệng, cửa quan, tai mắt, máu huyết sản nạn, buồn rầu")
            elif (sex==1 and a in sao2) or (sex==0 and a in sao5):
                print("- Thổ Tú: sao trung bình, chủ tiểu nhân, xuất hành không thuận, nhà cửa không vui, chăn nuôi thua lỗ")
            elif (sex==1 and a in sao3) or (sex==0 and a in sao9):
                print("- Thủy Diệu: sao trung bình, chủ Tài, Lộc, Hỷ; chủ pḥng việc đi sông nước và điều ăn tiếng nói")
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
    #Bảng coi hạn:
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
            print("Vậy nên bạn cũng đừng quá lo lắng nhé!")
    elif select11=='b' or select11=='B':
        print("b) CÁCH TIỄN SAO XẤU VÀ NGHÊNH SAO TỐT")
        print("*Hăy nhập thông tin của bạn!")
        while True:
            try:
                a=int(input("*Số tuổi của bạn: "))
                sex=int(input("*Giới tính của bạn (Nam/Nữ: 1/0): "))
                break
            except ValueError:
                print(e)
        print("-"*20)
        if a<10 or a>99 or sex>1 or sex<0:
            print(e,"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 10 đến 99)")
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
            print("- Bài vị:",bv,"\n- Khấn:\n",k,"\n- Cách cúng:",cc,"(cách bài trí các ngọn đèn xem tại mục 11.c)")
    elif select11=='c' or select11=='C':
        print("c) CỬU DIỆU TINH (SƠ ĐỒ BÀY ĐÈN CÚNG SAO)")
        print("*Hăy nhập thông tin của bạn!")
        while True:
            try:
                a=int(input("*Số tuổi của bạn: "))
                sex=int(input("*Giới tính của bạn (Nam/Nữ: 1/0): "))
                break
            except ValueError:
                print(e)
        print("-"*20)
        if a<10 or a>99 or sex>1 or sex<0:
            print(e,"\n(*Lưu ý: yêu cầu độ tuổi chỉ từ 10 đến 99)")
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
            else:
                print("\t\t Mộc Đức")
                print("\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *  *  *\n\t\t *\n\t\t    *\n\t\t       *\n\t\t    *\n\t\t *")
    else:
        print(e)
                    
##Thiên can:
if select==4:
    print("4: THIÊN CAN")
    while True:
      try:
        tc=input("*Nhập thiên can của bạn (ví dụ: Giáp, Ất,...): ")
        break
      except ValueError:
        print(e)  
    if tc in can1 or tc in can3 or tc in can5 or tc in can7 or tc in can9:
        print(ad,tc,"thuộc Dương")
    elif tc in can0 or tc in can2 or tc in can4 or tc in can6 or tc in can8:
        print(ad,tc,"thuộc Âm")
    if tc in can1 or tc in can2:
        print(nh,tc,"thuộc Mộc")
    elif tc in can3 or tc in can4:
        print(nh,tc,"thuộc Hoả")
    elif tc in can5 or tc in can6:
        print(nh,tc,"thuộc Thổ")
    elif tc in can7 or tc in can8:
        print(nh,tc,"thuộc Kim")
    elif tc in can0 or tc in can9:
        print(nh,tc,"thuộc Thuỷ")
    if tc in can1:
        print("+ Hợp:",can[6],"\n+ Phá:",can[5],"\n+ Xung:",can[7])
    elif tc in can2:
        print("+ Hợp:",can[7],"\n+ Phá:",can[6],"\n+ Xung:",can[8])
    elif tc in can3:
        print("+ Hợp:",can[8],"\n+ Phá:",can[7],"\n+ Xung:",can[9])
    elif tc in can4:
        print("+ Hợp:",can[9],"\n+ Phá:",can[8],"\n+ Xung:",can[0])
    elif tc in can5:
        print("+ Hợp:",can[0],"\n+ Phá:",can[9],"\n+ Xung:",can[1])
    elif tc in can6:
        print("+ Hợp:",can[1],"\n+ Phá:",can[0],"\n+ Xung:",can[2])
    elif tc in can7:
        print("+ Hợp:",can[2],"\n+ Phá:",can[1],"\n+ Xung:",can[3])
    elif tc in can8:
        print("+ Hợp:",can[3],"\n+ Phá:",can[2],"\n+ Xung:",can[4])
    elif tc in can9:
        print("+ Hợp:",can[4],"\n+ Phá:",can[3],"\n+ Xung:",can[5])
    elif tc in can0:
        print("+ Hợp:",can[5],"\n+ Phá:",can[4],"\n+ Xung:",can[6])
    else:
        print(e)

##Địa chi:
if select==5:
    print("5: ĐỊA CHI")
    while True:
      try:
        dc=input("*Nhập địa chi của bạn (hay còn gọi là con giáp): ")
        break
      except ValueError:
        print(e)  
    if dc in chi1 or dc in chi3 or dc in chi5 or dc in chi7 or dc in chi9 or dc in chi11:
        print(ad,dc,"thuộc Dương")
    elif dc in chi0 or dc in chi2 or dc in chi4 or dc in chi6 or dc in chi8 or dc in chi10:
        print(ad,dc,"thuộc Âm")
    if dc in chi3 or dc in chi4:
        print(nh,dc,"thuộc Mộc")
    elif dc in chi6 or dc in chi7:
        print(nh,dc,"thuộc Hoả")
    elif dc in chi9 or dc in chi10:
        print(nh,dc,"thuộc Kim")
    elif dc in chi0 or dc in chi1:
        print(nh,dc,"thuộc Thuỷ")
    elif dc in chi2 or dc in chi5 or dc in chi8 or dc in chi11:
        print(nh,dc,"thuộc Thổ")
    h2="+ Nhị hợp:"
    h3="+ Tam hợp:"
    lx="+ Lục xung:"
    if dc in chi0 or dc in chi3:
        print(h2,chi[3],"-",chi[0])
    elif dc in chi1 or dc in chi2:
        print(h2,chi[1],"-",chi[2])
    elif dc in chi4 or dc in chi11:
        print(h2,chi[4],"-",chi[11])
    elif dc in chi5 or dc in chi10:
        print(h2,chi[5],"-",chi[10])
    elif dc in chi6 or dc in chi9:
        print(h2,chi[6],"-",chi[9])
    elif dc in chi7 or dc in chi8:
        print(h2,chi[7],"-",chi[8])
    if dc in chi9 or dc in chi1 or dc in chi5:
        print(h3,chi[9],"-",chi[1],"-",chi[5])
    elif dc in chi0 or dc in chi4 or dc in chi8:
        print(h3,chi[0],"-",chi[4],"-",chi[8])
    elif dc in chi3 or dc in chi7 or dc in chi11:
        print(h3,chi[3],"-",chi[7],"-",chi[11])
    elif dc in chi6 or dc in chi10 or dc in chi2:
        print(h3,chi[6],"-",chi[10],"-",chi[2])
    if dc in chi3 or dc in chi9:
        print(lx,chi[9],"-",chi[3])
    elif dc in chi1 or dc in chi7:
        print(lx,chi[1],"-",chi[7])
    elif dc in chi4 or dc in chi10:
        print(lx,chi[4],"-",chi[10])
    elif dc in chi11 or dc in chi5:
        print(lx,chi[5],"-",chi[11])
    elif dc in chi0 or dc in chi6:
        print(lx,chi[0],"-",chi[6])
    elif dc in chi8 or dc in chi2:
        print(lx,chi[8],"-",chi[2])
    else:
        print(e)
##Xem dương lịch:
if select==6:
        import math
        y = int(input("Nhập năm: "))
        if y<1: 
            print(e)
        else:
            m = int(input("Nhập tháng: "))
            if m<1 or m>12:
                print(e)
            else:
                d = int(input("Nhập ngày: "))
                if d<1 or d>31 or (y%400!=0 and m==2 and d>29):
                    print(e)
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
                        print("Ngày thứ",d,"trong năm")
                        print("Tuần thứ",w,"trong năm")
     #Nhập ngày, tháng, năm ra thứ:
                    Thu=(d2+2*m+(3*(m+1))/5+y+(y/4))%7
                    if (m<3):
                        m+=12
                        y-=1
                    if math.ceil(Thu)==1:
                        print("Chủ nhật")
                    else:
                        print("Thứ: ",math.ceil(Thu))

##Lịch can chi:
if select==7:
   print("7: ÂM LỊCH")
   print("- Năm\n- Tháng\n- Ngày\n- Giờ")
   print("-"*20)
   while True:
      try:
        y=int(input("*Nhập năm: "))
        break
      except ValueError:
        print(e)
   x=y%10
   z=y%12
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
        print(e)
##Ngày hoàng đạo, hắc đạo:
if select==8:
        print("8: NGÀY HOÀNG DẠO, NGÀY HẮC ĐẠO")
        print("*Trong một tháng đều có 4 ngày Hoàng đạo và 4 ngày Hắc đạo: ")
        print("- Ngày Hoàng đạo: tốt, có thể cưới gả, chôn cất, đám tang, cải táng, làm nhà, mở cửa hàng, cửa hiệu, đi xa...")
        print("- Ngày Hắc đạo: không nên làm việc lớn, tối kỵ việc cưới gả, an táng, làm nhà, làm bếp...")
        print("*Bây giờ, hăy nhập thông tin của bạn!")
        print("(để tiện cho việc tính toán, xin quy ước đánh số ngày âm lịch như sau: Tý-1, Sửu-2, Dần-3, Măo-4, Thìn-5, Tỵ-6, Ngọ-7, Mùi-8, Thân-9, Dậu-10, Tuất-11, Hợi-12)")
        print("-"*20)
        m=int(input("*Nhập tháng âm lịch: "))
        if m<1 or m>12:
            print(e)
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
            option8=input("Bạn có muốn xem giờ hoàng đạo không?(Y/N): ") # điều kiện
            if option8=='Y' or option8=='y':
                d=int(input("*Nhập ngày âm lịch (1-12): "))
                if d<1 or d>12:
                    print(e)
                else:
                    hd3="- Giờ hoàng đạo là: "
                    if d==3 or d==9:
                        print(hd3,chi[1],chi[2],chi[5],chi[6],chi[8],chi[11])
                    elif d==4 or d==10:
                        print(hd3,chi[1],chi[3],chi[4],chi[7],chi[8],chi[10])
                    elif d==5 or d==11:
                        print(hd3,chi[3],chi[5],chi[6],chi[9],chi[10],chi[0])
                    elif d==6 or d==12:
                        print(hd3,chi[2],chi[5],chi[6],chi[7],chi[8],chi[0])
                    elif d==1 or d==7:
                        print(hd3,chi[1],chi[2],chi[4],chi[7],chi[8],chi[9])
                    else:
                        print(hd3,chi[3],chi[4],chi[6],chi[9],chi[10],chi[0])
            elif option8=='N' or option8=='n':
                print()
            else:
                print(e)
 
##Hung niên, tam tai:                   
if select==9:
        print("9: HUNG NIÊN, TAM TAI")
        print("*Giải thích: Hung niên, tam tai là gì?")
        print("- Hung niên, tam tai là những năm rơi vào sao chiếu mệnh không có lợi, đặc biệt về việc hôn nhân, cưới gả và cất nhà, xây dựng nhà cửa.")
        print("- Hung niên: chớ lập gia đình, thận trọng trong việc giao dịch kinh doanh. Tiến hành cất nhà ở tuổi này cũng được nhưng không tốt lắm.")
        print("- Tam tai: kỵ cất nhà và cưới gả (năm tam tai thường là của tuổi con trai, tuổi con gái thì không sao vì phần làm nhà là phần của người nam.")
        print("*Bây giờ, hăy nhập thông tin của bạn!")
        print("-"*20)
        y=input("*Nhập tuổi của bạn: ")
        hn="- Tuổi hung niên là: "
        tt="- Năm tam tai là: "
        if y in chi1:
            print(hn,chi[4])
        elif y in chi2:
            print(hn,chi[2])
        elif y in chi3:
            print(hn,chi[9])
        elif y in chi4 or y in chi7:
            print(hn,chi[10])
        elif y in chi5:
            print(hn,chi[5])
        elif y in chi6 or y in chi0:
            print(hn,chi[0])
        elif y in chi8 or y in chi11:
            print(hn,chi[11])
        elif y in chi9:
            print(hn,chi[3])
        else:
            print(hn,chi[1])
        if y in chi1 or y in chi5 or y in chi9:
            print(tt,chi[3],chi[4],chi[5])
        elif y in chi3 or y in chi7 or y in chi11:
            print(tt,chi[9],chi[10],chi[11])
        elif y in chi2 or y in chi6 or y in chi10:
            print(tt,chi[0],chi[1],chi[2])
        else:
            print(tt,chi[6],chi[7],chi[8])
i=input("Thank you!")
