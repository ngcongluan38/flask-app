# Histogram equalization
# Giới thiệu
 Thuật toán histogram equalization là một kỹ thuật xử lý ảnh được sử dụng để cải thiện độ tương phản trong hình ảnh. Mục tiêu chính của thuật toán này là làm phân phối các mức xám trên toàn bức ảnh trở nên đồng đều hơn, từ đó tăng cường độ tương phản và chi tiết trong hình ảnh.
1. Tính toán histogram: Đầu tiên, xây dựng histogram của ảnh để biết tần suất xuất hiện của mỗi mức xám.
2. Tính toán cumulative distribution function (CDF): Tính toán hàm phân phối tích lũy của histogram.
3. Normalization: Chuẩn hóa giá trị của CDF để đưa chúng về khoảng giá trị mức xám (thông thường từ 0 đến 255).
4. Mapping: Ánh xạ các giá trị mức xám cũ sang giá trị mới đã được chuẩn hóa. Quá trình này làm thay đổi phân bố các mức xám trên toàn bức ảnh.
# Áp dụng
Histogram equalization được áp dụng trong nhiều ứng dụng xử lý ảnh để cải thiện chất lượng hình ảnh và làm nổi bật các đặc trưng quan trọng. Dưới đây là một số mục đích chính khi áp dụng thuật toán histogram equalization:
1. Tăng cường độ tương phản: Histogram equalization giúp tăng cường độ tương phản trong hình ảnh bằng cách phân phối lại giá trị mức xám, làm cho các đối tượng và chi tiết trở nên dễ nhận biết hơn.
2. Cải thiện chi tiết: Khi áp dụng histogram equalization, các chi tiết trong hình ảnh thường trở nên rõ ràng hơn do đồng đều hóa phân bố mức xám.
3. Loại bỏ độ chênh lệch màu sắc: Trong một số trường hợp, ảnh có thể bị chệch màu sắc do ánh sáng không đồng đều. Histogram equalization có thể giúp cân bằng màu sắc và làm cho hình ảnh trở nên tự nhiên hơn.
4. Tăng cường hiệu suất các thuật toán xử lý ảnh: Trong nhiều ứng dụng như nhận diện đối tượng, nhận biết khuôn mặt, và xử lý ảnh y tế, việc cải thiện độ tương phản có thể giúp các thuật toán hoạt động hiệu quả hơn.
5. Hiển thị hình ảnh trên các thiết bị đồng nhất: Khi hiển thị hình ảnh trên các thiết bị khác nhau có độ sáng khác nhau, histogram equalization có thể giúp duy trì chất lượng hình ảnh và hiển thị tốt trên nhiều loại màn hình.
# Ưu điểm
1. Cải thiện Độ Tương Phản
2. Dễ Thực Hiện
3. Không Yêu Cầu Thêm Thông Tin Ngoại Vi
4. Tích Lũy Tích Lũy (CDF) Monotonically Tăng
# Nhược điểm
1. Nhiễu Tăng Cao
2. Mất Mát Thông Tin
3. Không Phù Hợp Cho Tất Cả Các Loại Ảnh
4. Không Tùy Chỉnh Được Đối Với Các Khu Vực Cụ Thể
# Code
Kiểm tra số chiều của ảnh
Trong trường hợp ảnh có 3 chiều, có thể nói rằng nó là một ảnh màu (với chiều thứ ba là các kênh màu: B, G, R). Trong trường hợp này, mã chuyển đổi ảnh màu sang ảnh xám bằng cách sử dụng cv2.cvtColor với mã màu cv2.COLOR_BGR2GRAY. Điều này giúp đảm bảo rằng histogram equalization sẽ được áp dụng cho ảnh xám.
 
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_equalized = cv2.equalizeHist(img)
    return img_equalized

Áp dụng thuật toán
  
    img_equalized = histogram_equalization_cv2(img)

Chạy localhost ở port 5000

    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        app.run(debug=True, port=port)

