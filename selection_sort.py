

# Install dependencies and Manim
# !pip install manim

# Import and create the animation
from manim import *
import numpy as np

# Configuration for rendering
config.media_width = "75%"
config.verbosity = "WARNING"

class SelectionSort(Scene):
    def construct(self):
        # Create the array visualization
        arr = [5, 2, 8, 12, 1, 6, 3]  # Array to be sorted
        n = len(arr)
        
        # Title
        title = Text("Selection Sort Algorithm").to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # Create visualization for array items
        squares = []
        labels = []
        
        # Create a group of squares with values
        for i, val in enumerate(arr):
            square = Square(side_length=1).set_fill(BLUE, opacity=0.5)
            label = Text(str(val)).scale(0.8)
            
            square.move_to([i*1.2 - (n-1)*1.2/2, 0, 0])
            label.move_to(square.get_center())
            
            squares.append(square)
            labels.append(label)
        
        # Create groups
        squares_group = VGroup(*squares)
        labels_group = VGroup(*labels)
        
        # Show initial array
        self.play(
            Create(squares_group),
            Write(labels_group)
        )
        
        # Status text
        status = Text("Starting Selection Sort").scale(0.8).to_edge(DOWN, buff=1)
        self.play(Write(status))
        
        # Run Selection Sort
        for i in range(n):
            # Highlight current position
            self.play(
                squares[i].animate.set_fill(YELLOW, opacity=0.5),
                status.animate.become(
                    Text(f"Finding minimum in positions {i} to {n-1}").scale(0.8).to_edge(DOWN, buff=1)
                )
            )
            
            # Find minimum element
            min_idx = i
            min_marker = Triangle().scale(0.2).set_fill(RED, opacity=1)
            min_marker.next_to(squares[min_idx], UP, buff=0.3)
            self.play(Create(min_marker))
            
            # Search for minimum in remaining array
            for j in range(i+1, n):
                # Highlight element being compared
                self.play(
                    squares[j].animate.set_fill(PURPLE, opacity=0.5),
                    status.animate.become(
                        Text(f"Comparing {arr[min_idx]} with {arr[j]}").scale(0.8).to_edge(DOWN, buff=1)
                    )
                )
                
                # If current element is smaller than minimum
                if arr[j] < arr[min_idx]:
                    # Reset previous minimum highlight
                    self.play(
                        squares[min_idx].animate.set_fill(BLUE, opacity=0.5)
                    )
                    
                    # Update minimum
                    min_idx = j
                    self.play(
                        min_marker.animate.next_to(squares[min_idx], UP, buff=0.3),
                        squares[min_idx].animate.set_fill(RED, opacity=0.5),
                        status.animate.become(
                            Text(f"New minimum: {arr[min_idx]}").scale(0.8).to_edge(DOWN, buff=1)
                        )
                    )
                else:
                    # Reset current comparison
                    self.play(
                        squares[j].animate.set_fill(BLUE, opacity=0.5)
                    )
            
            # Swap if needed
            if min_idx != i:
                # Update status
                self.play(
                    status.animate.become(
                        Text(f"Swapping {arr[i]} and {arr[min_idx]}").scale(0.8).to_edge(DOWN, buff=1)
                    )
                )
                
                # Swap in array
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                
                # Animate swap
                self.play(
                    labels[i].animate.become(Text(str(arr[i])).scale(0.8).move_to(squares[i].get_center())),
                    labels[min_idx].animate.become(Text(str(arr[min_idx])).scale(0.8).move_to(squares[min_idx].get_center())),
                    squares[i].animate.set_fill(GREEN, opacity=0.5),
                    squares[min_idx].animate.set_fill(BLUE, opacity=0.5),
                    FadeOut(min_marker)
                )
            else:
                # No swap needed
                self.play(
                    status.animate.become(
                        Text(f"{arr[i]} is already in the correct position").scale(0.8).to_edge(DOWN, buff=1)
                    ),
                    squares[i].animate.set_fill(GREEN, opacity=0.5),
                    FadeOut(min_marker)
                )
        
        # Show sorting is complete
        self.play(
            status.animate.become(
                Text("Array is sorted!").scale(0.8).to_edge(DOWN, buff=1)
            )
        )
        
        # Add description of time complexity
        complexity = VGroup(
            Text("Time Complexity: O(n²)"),
            Text("Space Complexity: O(1)")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7).to_edge(UP, buff=1.5)
        
        self.play(Write(complexity))
        
        self.wait(2)

# Run the scene
scene = SelectionSort()
scene.render()


# Display the video
from IPython.display import Video, HTML
video = Video("media/videos/1080p60/SelectionSort.mp4", embed=True, width=800)
HTML(video._repr_html_())
