import asyncio
import threading

class Vivarium:
    """
    Vivarium class represents a container for managing ingress and egress of data.
    It provides synchronized access to the ingress and egress lists using locks.

    Attributes:
        ingress_list (list): A list to store incoming data.
        egress_list (list): A list to store outgoing data.
        ingress_lock (Lock): A lock for synchronizing access to the ingress_list.
        egress_lock (Lock): A lock for synchronizing access to the egress_list.
    """

    def __init__(self):
        """
        Initializes a new instance of the Vivarium class.
        """
        # Lists to store the ingress and egress data
        self.ingress_list = []
        self.egress_list = []

        # Locks to synchronize access to the ingress and egress lists
        self.ingress_lock = threading.Lock()
        self.egress_lock = threading.Lock()

        # Asyncio event loop.  Create an event loop object
        self.loop = asyncio.new_event_loop()

        # Set the current event loop for the current OS thread
        asyncio.set_event_loop(self.loop)


    async def async_input(self, prompt):
        """
        Asynchronous method to receive user input.
        """
        return await self.loop.run_in_executor(None, input, prompt)

    async def async_print(self, message):
        """
        Asynchronous method to print output.
        """
        await self.loop.run_in_executor(None, print, message)

    async def ingress(self):
        """
        Method representing the ingress thread.
        It allows users to input data and adds it to the ingress list.
        """
        while True:
            user_input = await self.async_input("Enter input: ")

            # Acquire the ingress lock to ensure synchronized access
            with self.ingress_lock:
                self.ingress_list.append(user_input)

    async def egress(self):
        """
        Method representing the egress thread.
        It retrieves data from the egress list and prints it.
        """
        while True:
            # Acquire the egress lock to ensure synchronized access
            with self.egress_lock:
                if self.egress_list:
                    output = self.egress_list.pop(0)
                    await self.async_print(output)

    def start_threads(self):
        """
        Starts the ingress and egress threads.
        """
        self.loop.run_until_complete(asyncio.gather(
            self.ingress(),
            self.egress()
        ))

    def stop_threads(self):
        """
        Stops the ingress and egress threads by stopping the event loop.
        """
        self.loop.stop()
        self.loop.close()

    def read_ingress_list(self):
        """
        Returns a copy of the ingress list.
        """
        with self.ingress_lock:
            return self.ingress_list.copy()

    def write_to_egress_list(self, data):
        """
        Adds the given data to the egress list.
        """
        with self.egress_lock:
            self.egress_list.append(data)
