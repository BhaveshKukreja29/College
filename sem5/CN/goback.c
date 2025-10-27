// go_back_n.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // --- HARDCODED VALUES ---
    int total_frames = 12;
    int window_size = 4; // This is 'N' in Go-Back-N
    
    int sent_frames = 0;
    int acked_frames = 0;
    
    srand(time(NULL)); // Seed for random number generation

    while (acked_frames < total_frames) {
        // --- SENDER ---
        printf("--- Sending Window ---\n");
        for (int i = acked_frames; i < acked_frames + window_size && i < total_frames; i++) {
            printf("Sending frame %d...\n", i);
            sent_frames++;
        }

        // --- SIMULATE NETWORK & RECEIVER ---
        // Let's pretend a frame is lost. 1 in 3 chance of losing a frame.
        int lost_frame = -1; // -1 means no loss
        if (rand() % 3 == 0) { // Randomly decide if a frame is lost
            lost_frame = acked_frames + (rand() % window_size);
            if (lost_frame >= total_frames) {
                lost_frame = -1; // Don't lose a frame that doesn't exist
            }
        }

        if (lost_frame == -1) {
            // --- SUCCESS CASE ---
            acked_frames += window_size;
            if (acked_frames > total_frames) {
                acked_frames = total_frames;
            }
            printf("\n>>> SUCCESS: Received ACK for all frames up to %d.\n\n", acked_frames - 1);
        } else {
            // --- ERROR CASE (GO-BACK-N) ---
            printf("\n>>> ERROR: Frame %d was lost!\n", lost_frame);
            printf(">>> Receiver discards all frames from %d onwards.\n", lost_frame);
            printf(">>> Sender timer expires. GOING BACK TO FRAME %d.\n\n", lost_frame);
            acked_frames = lost_frame; // The sender must "go back" to the lost frame
        }
    }

    printf("All frames have been successfully sent and acknowledged.\n");
    printf("Total frames sent (including retransmissions): %d\n", sent_frames);

    return 0;
}