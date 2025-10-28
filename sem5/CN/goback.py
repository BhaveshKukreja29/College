def go_back_n_simulation():
    total_frames = int(input("Enter the total number of frames: "))
    window_size = int(input("Enter the window size (N): "))
    
    sent_frames = 0
    ack_received_up_to = -1
    
    while ack_received_up_to < total_frames - 1:
        # Send a window of frames
        for i in range(ack_received_up_to + 1, min(ack_received_up_to + 1 + window_size, total_frames)):
            print(f"Sender: Sent Frame {i}")
            sent_frames += 1

        # Simulate receiving acknowledgements
        print("\n--- Receiver Side ---")
        lost_frame = int(input(f"Enter the frame number that was lost or corrupted (-1 for none): "))
        
        if lost_frame == -1 or lost_frame > ack_received_up_to + window_size:
            # All frames in the window were received successfully
            ack_received_up_to += window_size
            print(f"Receiver: All frames in window received. ACK for frame {ack_received_up_to} sent.\n")
        else:
            # A frame was lost
            ack_received_up_to = lost_frame - 1
            print(f"Receiver: Frame {lost_frame} was not received correctly.")
            print(f"Sender: Timeout for Frame {lost_frame}. Going back and re-transmitting.\n")
    
    print("All frames have been successfully transmitted.")
    print(f"Total frames sent (including retransmissions): {sent_frames}")

# --- Start Simulation ---
go_back_n_simulation()