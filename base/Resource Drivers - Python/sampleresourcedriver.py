import qualidriver

class SampleResourceDriver:
    
    def __init__(self):
        pass

    # Initialize the driver session, this function is called everytime a new instance of the driver is created
    # This is a good place to load and cache the driver configuration, initiate sessions etc.
    def initialize(self, context):              
        """
        :type context: qualidriver.InitCommandContext
        """
        return 'Finished initializing'

    # Destroy the driver session, this function is called everytime a driver instance is destroyed
    # This is a good place to close any open sessions, finish writing to log files
    def cleanup(self):
        pass
    
    # A command with a single parameter
    def example_command1(self, user_param1):     
        return result

    # An advanced command that receives information from CloudShell server (context param)
    def example_command2(self, context, user_param1, user_param2, user_param3):     
        """
        :type context: qualidriver.ResourceCommandContext
        """   
        result = self._helper_method(user_param1)
        return result
    
    # An advanced command that that supports cancellation
    # Adding the cancellation_token param will result in a "stop" button that will be available to the end user from the web interface.
    def example_command3(self, context, cancellation_token, user_param1, user_param2, user_param3):     
        """
        :type context: qualidriver.ResourceCommandContext
        :type cancellation_token: qualidriver.CancellationContext
        """
        result = self._helper_method(user_param1)
        return result 
    
    # private functions are always hidden
    def _helper_method(title):
        return "---====%s====---" % title
