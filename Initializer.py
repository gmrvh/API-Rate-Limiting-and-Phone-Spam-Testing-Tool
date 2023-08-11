class workerObject:

    def __init__(self, workerName, workerMode, workerType, workerDPC, workerDPB, burst, workerMax, workerURL,workerBypassMethod,workerStatus,workerIsActive,workerHeader,workerParameters, workerSuccessText, workerPrefix,google_token,seleniummBypass ):
        self.workerName = workerName
        self.workerMode = workerMode
        self.workerType = workerType
        self.workerDPC = workerDPC
        self.workerDPB = workerDPB
        self.burst = burst
        self.workerMax = workerMax
        self.workerURL = workerURL
        self.workerBypassMethod = workerBypassMethod
        self.workerStatus = workerStatus
        self.workerIsActive = workerIsActive
        self.workerHeader = workerHeader
        self.workerParameters = workerParameters
        self.workerSuccessText = workerSuccessText
        self.workerPrefix = workerPrefix
        self.google_token = google_token
        self.seleniumBypass = seleniummBypass
    hit = 0
    miss = 0
    total = hit + miss
    validated_cookie = {}
    twocaptcha_token = 0
    
    workerStateRunning = False

class targetObject:
    def __init__(self, num, max):
        self.num = num
        self.max = max

    sms_workers_allocated = []
    call_workers_allocated = []
    all_workers_allocated = sms_workers_allocated + call_workers_allocated
    count = 0
    call_hit = 0
    call_miss = 0
    sms_hit = 0
    sms_miss = 0