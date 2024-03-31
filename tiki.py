import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from metro import *

green_line_stations =[ 14,'Nagasandra', 'Dasarahalli', 'Jalahalli', 'Peenya_Industry', 'Peenya', 'Goraguntepalya', 'Yeshwanthpura', 'Sandal_Soap_Factory', 'Mahalakshmi', 'Rajajinagara', 'Kuvempu_Road', 'Srirampura', 'Sampige_Road', 'Nadaprabhu_Kempegowda_station_(Majestic)', 'Chikkapette', 'Krishna_Rajendra_Market', 'National_College', 'Lalbagh_Botanical_Garden', 'South_End_Circle', 'Jayanagara', 'Rashtreeya_Vidyalaya_Road', 'Banashankari', 'Jaya_Prakash_Nagara', 'Yelachenahalli', 'Konanakunte_Cross', 'Doddakallasandra', 'Vajarahalli', 'Talaghattapura', 'Silk_Institute','Whitefield_(Kadugodi)', 'Hopefarm_Channasandra', 'Kadugodi_Tree_Park', 'Pattanduru_Agrahara', 'Sri_Sathya_Sai_Hospital', 'Nallurhalli', 'Kundalahalli', 'Seetharamapalya', 'Hoodi', 'Garudacharapalya', 'Singayyanapalya', 'Krishnarajapura_(K.R.Pura)', 'Benniganahalli', 'Baiyappanahalli', 'Swami_Vivekananda_Road', 'Indiranagara', 'Halasuru', 'Trinity', 'MG_Road', 'Cubbon_Park', 'Dr._BR._Ambedkar_Station_(Vidhana_Soudha)', 'Sir_M._Visveshwaraya_Station_(Central_College)', 'Nadaprabhu_Kempegowda_station_(Majestic)', 'City_Railway_station', 'Magadi_Road', 'Sri_Balagangadharanatha_Swamiji_Station_(Hosahalli)', 'Vijayanagara', 'Attiguppe', 'Deepanjali_Nagara', 'Mysuru_Road', 'Pantharapalya_(Nayandahalli)', 'Rajarajeshwari_Nagar', 'Jnanabharathi', 'Pattanagere', 'Kengeri_Bus_Terminal', 'Kengeri', 'Challaghatta']
purple_line_stations = [14,'Nagasandra', 'Dasarahalli', 'Jalahalli', 'Peenya_Industry', 'Peenya', 'Goraguntepalya', 'Yeshwanthpura', 'Sandal_Soap_Factory', 'Mahalakshmi', 'Rajajinagara', 'Kuvempu_Road', 'Srirampura', 'Sampige_Road', 'Nadaprabhu_Kempegowda_station_(Majestic)', 'Chikkapette', 'Krishna_Rajendra_Market', 'National_College', 'Lalbagh_Botanical_Garden', 'South_End_Circle', 'Jayanagara', 'Rashtreeya_Vidyalaya_Road', 'Banashankari', 'Jaya_Prakash_Nagara', 'Yelachenahalli', 'Konanakunte_Cross', 'Doddakallasandra', 'Vajarahalli', 'Talaghattapura', 'Silk_Institute','Whitefield_(Kadugodi)', 'Hopefarm_Channasandra', 'Kadugodi_Tree_Park', 'Pattanduru_Agrahara', 'Sri_Sathya_Sai_Hospital', 'Nallurhalli', 'Kundalahalli', 'Seetharamapalya', 'Hoodi', 'Garudacharapalya', 'Singayyanapalya', 'Krishnarajapura_(K.R.Pura)', 'Benniganahalli', 'Baiyappanahalli', 'Swami_Vivekananda_Road', 'Indiranagara', 'Halasuru', 'Trinity', 'MG_Road', 'Cubbon_Park', 'Dr._BR._Ambedkar_Station_(Vidhana_Soudha)', 'Sir_M._Visveshwaraya_Station_(Central_College)', 'Nadaprabhu_Kempegowda_station_(Majestic)', 'City_Railway_station', 'Magadi_Road', 'Sri_Balagangadharanatha_Swamiji_Station_(Hosahalli)', 'Vijayanagara', 'Attiguppe', 'Deepanjali_Nagara', 'Mysuru_Road', 'Pantharapalya_(Nayandahalli)', 'Rajarajeshwari_Nagar', 'Jnanabharathi', 'Pattanagere', 'Kengeri_Bus_Terminal', 'Kengeri', 'Challaghatta']

def distance(source, destination):
    if source in green_line_stations and destination in green_line_stations:
        return abs(green_line_stations.index(source) - green_line_stations.index(destination))
    elif source in purple_line_stations and destination in purple_line_stations:
        return abs(purple_line_stations.index(source) - purple_line_stations.index(destination))
    elif source in purple_line_stations and destination in green_line_stations:
        p = abs(purple_line_stations.index(source) - purple_line_stations.index(purple_line_stations[0]))
        g = abs(green_line_stations.index(destination) - green_line_stations.index(green_line_stations[0]))
        return p + g
    elif source in green_line_stations and destination in purple_line_stations:
        g = abs(green_line_stations.index(source) - green_line_stations.index(green_line_stations[0]))
        p = abs(purple_line_stations.index(destination) - purple_line_stations.index(purple_line_stations[0]))
        return g + p
    else:
        print("Invalid Station Name")

def result():
    current_location = current_location_combobox.get()
    destination = destination_combobox.get()

    print("Current Location:", current_location)
    print("Destination:", destination)

    print("Data type of Current Location:", type(current_location))
    print("Data type of Destination:", type(destination))

    if current_location in green_line_stations or current_location in purple_line_stations:
        if destination in green_line_stations or destination in purple_line_stations:
            dist = distance(current_location, destination)
            info_label.config(text=f"Distance: {dist} units\n Estimated time : {dist*2.5} min \n Estimated cost : {round(dist/3*2.72)} Rupees", fg="black")
        else:
            info_label.config(text="Invalid Destination Station", fg="red")
    else:
        info_label.config(text="Invalid Current Location Station", fg="red")


app = tk.Tk()
app.geometry("500x550")
app.title("Metro System")
app.config(bg='#808080')

img = Image.open("metrologo.png")
img = img.resize((150, 120))
tk_img = ImageTk.PhotoImage(img)

label = tk.Label(app, text="Namma Metro", bg='#808080', fg='white', font=('Helvetica', 25))
label.pack(pady=20)

frame = tk.Frame(master=app, bg='#34495e')
frame.pack(pady=20, padx=40, fill='both', expand=True)

image_label = tk.Label(master=frame, image=tk_img, bg='#34495e')
image_label.pack(pady=15, padx=10)

current_location_combobox = ttk.Combobox(frame, values=green_line_stations, font=('System', 12))
current_location_combobox.set("Select Current Location")
current_location_combobox.pack(pady=12, padx=10)

destination_combobox = ttk.Combobox(frame, values=purple_line_stations, font=('System', 12))
destination_combobox.set("Select Destination")
destination_combobox.pack(pady=12, padx=10)

button = tk.Button(master=frame, text='Calculate', command=result, bg='#2980b9', fg='white', font=('Helvetica', 12), bd=0, relief='flat')
button.pack(pady=12, padx=10)
button.configure(borderwidth=1, relief='solid')

info_label = tk.Label(frame, text="", fg='#34495e', font=('System', 12))
info_label.pack(pady=10)

app.mainloop()
