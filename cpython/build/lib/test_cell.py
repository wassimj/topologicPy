import Cell, CellUtility

if __name__ == '__main__':
    cell = CellUtility.ByCuboid(
			0, # const double kXCentroid, 
            0, # const double kYCentroid, 
            0, # const double kZCentroid,
			0, # const double kXDimension, 
            0, # const double kYDimension, 
            0, # const double kZDimension,
			0, # const double kXNormal, 
            0, # const double kYNormal, 
            0, # const double kZNormal,
			0, # const double kXAxisX, 
            0, # const double kYAxisX, 
            0, # const double kZAxisX,
			0, # const double kXAxisY, 
            0, # const double kYAxisY, 
            0 # const double kZAxisY
            )
    if cell.IsContainerType():
        print("Not container")
    else:
        print("It is container")
