class PDController:
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.prev_error = 0  # Previous error initialized to 0

    def compute_action(self, reference, output):
        # Calculate the error at the current time step
        error = reference - output
        
        # Calculate the change of the error
        error_change = error - self.prev_error
        
        # Calculate the control action
        action = self.kp * error + self.kd * error_change
        
        # Update the previous error for the next time step
        self.prev_error = error
        
        return action