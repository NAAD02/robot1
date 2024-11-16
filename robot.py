from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDIconButton

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        padding: [10, 20, 10, 10]
        # Tiêu đề
        BoxLayout:
            size_hint_y: None
            height: "80dp"
            canvas.before:
                Color:
                    rgba: 0, 0.3, 0.7, 1  
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDLabel:
                text: "Robot Hút Bụi Tự Động"
                halign: 'center'
                valign: 'middle'
                font_size: '24sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # Màu trắng

        # Layout chính
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 20
                      
            
            # Layout nút điều khiển
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: 0.3
                spacing: 10

                Widget:  

                BoxLayout:
                    size_hint_y: None
                    height: "70dp"  
                    spacing: 10
                    Widget:  
                    MDFillRoundFlatButton:
                        text: "Lên"
                        size_hint: (None, None)  
                        size: "100dp", "70dp"  
                        font_size: "24sp"
                        on_press: app.control_robot("up")
                    Widget:  

                
                BoxLayout:
                    size_hint_y: None
                    height: "70dp"
                    spacing: 50
                    pos_hint: {'center_x': 0.5}  
                    Widget:
                        size_hint_x: 0.25  
                    MDFillRoundFlatButton:
                        text: "Trái"
                        size_hint: (None, None)  
                        size: "100dp", "70dp"  
                        font_size: "24sp"
                        on_press: app.control_robot("left")
                    MDFillRoundFlatButton:
                        text: "Mic"
                        size_hint: (None, None)  
                        size: "100dp", "70dp"  
                        font_size: "24sp"
                        on_press: app.control_robot("mic")
                    MDFillRoundFlatButton:
                        text: "Phải"
                        size_hint: (None, None)  
                        size: "100dp", "70dp"  
                        font_size: "24sp"
                        on_press: app.control_robot("right")
                    Widget:
                        size_hint_x: 0.25  

                BoxLayout:
                    size_hint_y: None
                    height: "70dp"  
                    spacing: 10
                    Widget:  
                    MDFillRoundFlatButton:
                        text: "Xuống"
                        size_hint: (None, None)  
                        size: "100dp", "70dp"  
                        font_size: "24sp"
                        on_press: app.control_robot("down")
                    Widget:  

                Widget: 

           
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.1
                spacing: 20
                pos_hint: {'center_x': 0.5}  
                
                
                MDRaisedButton:
                    text: "AUTO"
                    size_hint: None, None
                    size: "200dp", "60dp"  
                    on_press: app.control_robot("auto")
                    md_bg_color: 1, 1, 0, 1  # Màu nền vàng
                    text_color: 0, 0, 0, 1  # Màu chữ đen
                    font_size: "24sp"  # Giữ kích thước giống như nút "Tốc độ"

                MDRaisedButton:
                    text: "HÚT"
                    size_hint: None, None
                    size: "200dp", "60dp"  # Kích thước cố định
                    on_press: app.control_robot("hút")
                    md_bg_color: 1, 1, 0, 1  # Màu nền vàng
                    text_color: 0, 0, 0, 1  # Màu chữ đen
                    font_size: "24sp"  # Giữ kích thước giống như nút "Tốc độ"

                MDRaisedButton:
                    text: "QUÉT"
                    size_hint: None, None
                    size: "200dp", "60dp"  
                    on_press: app.control_robot("quét")
                    md_bg_color: 1, 1, 0, 1  # Màu nền vàng
                    text_color: 0, 0, 0, 1  # Màu chữ đen
                    font_size: "24sp"  

                MDRaisedButton:
                    text: "OUT"
                    size_hint: None, None
                    size: "150dp", "60dp"
                    on_press: app.control_robot("out")
                    md_bg_color: 1, 0, 0, 1  # Màu nền đỏ cho nút OUT
                    text_color: 0, 0, 0, 1  # Màu chữ đen
                    font_size: "24sp"  
                Widget: 
           
            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: 0.1
                spacing: 20
                pos_hint: {'center_x': 0.5}  

                
                MDLabel:
                    text: "Tốc độ"
                    size_hint_x: 0.25
                    font_size: "24sp"  
                    color: 0, 0, 0, 1  
                    halign: 'left'  # Căn trái chữ "Tốc độ"

                Slider:
                    size_hint_x: 0.9
                    min: 0
                    max: 100
                    value: 50
                    pos_hint: {"x": 0}
                Widget: 
                    size_hint_x: 0.1
                   
                    
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def control_robot(self, direction):
        # Hàm xử lý sự kiện khi nhấn nút
        print(f"Điều khiển robot: {direction}")

MainApp().run()
