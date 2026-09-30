# Simple Reflex Vacuum Cleaner Agent

def reflex_vacuum_agent(location, status):
    """
    Simple Reflex Agent:
    - If the room is Dirty -> Suck
    - If the agent is in Room A and it is Clean -> Move Right
    - If the agent is in Room B and it is Clean -> Move Left
    """

    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Move Right"

    elif location == "B":
        return "Move Left"


def run_simulation():

    # Environment
    environment = {
        "A": "Dirty",
        "B": "Clean"
    }

    # Starting location
    current_location = "A"

    print("=" * 45)
    print("       SIMPLE REFLEX VACUUM AGENT")
    print("=" * 45)

    print("\nInitial Environment:")
    print(f"Room A : {environment['A']}")
    print(f"Room B : {environment['B']}")
    print(f"Agent  : Room {current_location}")

    # Run simulation
    for step in range(1, 4):

        print("\n" + "-" * 45)
        print(f"Step {step}")
        print("-" * 45)

        # Perceive the environment
        current_status = environment[current_location]

        print(f"Agent Location : Room {current_location}")
        print(f"Room Status    : {current_status}")

        # Decide action
        action = reflex_vacuum_agent(
            current_location,
            current_status
        )

        print(f"Agent Action   : {action}")

        # Perform action
        if action == "Suck":

            environment[current_location] = "Clean"
            print(f"Room {current_location} cleaned successfully!")

        elif action == "Move Right":

            current_location = "B"
            print("Agent moved from Room A to Room B.")

        elif action == "Move Left":

            current_location = "A"
            print("Agent moved from Room B to Room A.")

    # Final state
    print("\n" + "=" * 45)
    print("           SIMULATION COMPLETED")
    print("=" * 45)

    print("\nFinal Environment:")
    print(f"Room A : {environment['A']}")
    print(f"Room B : {environment['B']}")
    print(f"Agent  : Room {current_location}")


# Start the simulation
run_simulation()