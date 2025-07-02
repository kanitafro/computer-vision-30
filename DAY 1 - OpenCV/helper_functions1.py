import cv2

def show_coordinates(event, x, y, flags, param):
    """
    Displays mouse coordinates on an image.
    ---
    Args:
        param (dict): Must contain:
            - 'image': The image to display (numpy array)
            - 'window_name': Name of the OpenCV window
    """
    if event == cv2.EVENT_MOUSEMOVE:
        # Unpack parameters
        image = param['image']
        window_name = param['window_name']
        
        # Create a copy to avoid modifying the original
        img_with_coords = image.copy()
        
        # Display coordinates
        text = f"({x}, {y})"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        thickness = 1
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        
        # Position text at bottom-right
        text_x = img_with_coords.shape[1] - text_size[0] - 10
        text_y = img_with_coords.shape[0] - 10
        
        # Draw text (with outline for visibility)
        cv2.putText(img_with_coords, text, (text_x, text_y), font, font_scale, (0, 0, 0), thickness + 1, cv2.LINE_AA)
        cv2.putText(img_with_coords, text, (text_x, text_y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
        
        # Update the window
        cv2.imshow(window_name, img_with_coords)
