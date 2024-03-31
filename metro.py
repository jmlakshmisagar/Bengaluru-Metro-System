def distance(source, destination):
    # Check if source and destination are valid stations
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

    # Check data types of current_location and destination
    print("Data type of Current Location:", type(current_location))
    print("Data type of Destination:", type(destination))

    # Check if the selected stations are valid
    if current_location in green_line_stations or current_location in purple_line_stations:
        if destination in green_line_stations or destination in purple_line_stations:
            # Calculate distance only if stations are valid
            dist = distance(current_location, destination)
            info_label.config(text=f"Distance: {dist} units\n Estimated time : {dist*10} min \n Estimated cost : {round(dist/3*10)} Rupees", fg="black")
        else:
            info_label.config(text="Invalid Destination Station", fg="red")
    else:
        info_label.config(text="Invalid Current Location Station", fg="red")

