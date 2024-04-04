import time
import threading

runningP = -1
RN = {
    0: [0, 0, 0, 0, 0],
    1: [0, 0, 0, 0, 0],
    2: [0, 0, 0, 0, 0],
    3: [0, 0, 0, 0, 0],
    4: [0, 0, 0, 0, 0],
}
token = {"token_owner": 2, "Q": [], "LN": [0, 0, 0, 0, 0], "isRunning": False}
lock = threading.Lock()


def dispCurrentRNState():
    for key, value in RN.items():
        print(key, ": ", value)


def updateRN(processNo, sequenceNumber):
    for key, value in RN.items():
        value[processNo] = max(value[processNo], sequenceNumber)


def executeCS(processForCS):
    global token, runningP
    print("\n******************************\n")
    print(f"Process {processForCS} executing CS...")
    print("Token owner is: {}".format(token["token_owner"]))
    time.sleep(10)
    print(f"\nProcess {processForCS} has completed running CS")
    token["isRunning"] = False
    token["LN"][processForCS] = RN[processForCS][processForCS]
    
    with lock:
        for index, val in enumerate(RN[token["token_owner"]]):
            if val == token["LN"][index] + 1 and index != runningP and index not in token["Q"]:
                print(f"Process {index}'s request is outstanding, it will be added to Token's Queue")
                token["Q"].append(index)
                print(f'Queue: {token["Q"]}')
                
        if len(token["Q"]) != 0:
            poppedPs = token["Q"].pop(0)
            token["token_owner"] = poppedPs
            token["isRunning"] = True
            runningP = poppedPs
            thread = threading.Thread(target=executeCS, args=(poppedPs,))
            thread.start()


if __name__ == "__main__":
    print("Running Main Again")
    print("Current RN Arrays: ")
    dispCurrentRNState()
    print(" ")
    print("Token owner is: {}".format(token["token_owner"]))
    
    while True:
        if token["isRunning"]:
            print("-----------------")
            processes = input("Enter Process Numbers which want to access C.S separated by space (Click N for None): ")
            
            if processes != "N":
                psList = processes.strip().split(" ")
                print(" ")
                for ps in psList:
                    processForCS = int(ps)
                    print(f"***** Process {processForCS} *****")
                    seqNo = RN[processForCS][processForCS] + 1
                    print(f"Process No.: {processForCS}")
                    print(f"Sequence No.: {seqNo}")

                print(f"Broadcasting Request ({processForCS} , {seqNo}) .......")
                time.sleep(2)
                print("Broadcast complete")
                print(" ")
                print("Updating RN Arrays at all process sites")
                updateRN(processForCS, seqNo)
                print("Current RN Arrays: ")
                dispCurrentRNState()
                print(" ")
        else:
            processForCS = int(input("Enter Process No. which wants to access C.S: "))
            seqNo = RN[processForCS][processForCS] + 1
            print(f"Process No.: {processForCS}")
            print(f"Sequence No.: {seqNo}")
            print(f"Broadcasting Request ({processForCS} , {seqNo}) .......")
            time.sleep(2)
            print("Broadcast complete")
            print(" ")
            print("Updating RN Arrays at all process sites")
            updateRN(processForCS, seqNo)
            print("Current RN Arrays: ")
            dispCurrentRNState()
            print(" ")
            if RN[token["token_owner"]][processForCS] == token["LN"][processForCS] + 1:
                print(f"Conditions met, giving token to {processForCS}...")
                token["token_owner"] = processForCS
                print("Token owner is: {}".format(token["token_owner"]))
                token["isRunning"] = True
                runningP = processForCS
                thread = threading.Thread(target=executeCS, args=(processForCS,))
                thread.start()

                print("Main Continuing Running")
