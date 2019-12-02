
class UPIInputs:
    
    def getPlacementCost(inputs = {}):
        "Output is a float"
        output = {"Message": "getPlacementCost" , "Value" : 0}
        return output

    def getRTKM(inputs = {}):
        "Output is a int"
        output = {"Message": "getRTKM" , "Value" : 50}
        return output
        
    def runModel(inputs = {}):
        "Output is dataframe {Source,Dest, linkage}"
        output = {"Message": "runModel" , "Value" : pd.DataFrame(columns=['src','dest','link'])}
        return output
    
    def runSenario(inputs = {})
        "Output is dataframe {Source,Dest, linkage}"
        output = {"Message": "getPlacementCost" , "Value" : pd.DataFrame(columns=['src','dest','link'])}
        return output