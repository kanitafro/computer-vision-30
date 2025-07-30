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

def setup_mouse_callback(window_name, image):
    """
    Set up mouse callback to display coordinates and RGB values in a white footer below the image.
    
    Args:
        window_name (str): Name of the OpenCV window
        image (numpy.ndarray): The image to display (in BGR format)
    """
    # Create white footer area (50 pixels tall)
    footer_height = 50
    footer = np.full((footer_height, image.shape[1], 3), 255, dtype=np.uint8)  # White background
    
    # Combine image and footer
    display_image = np.vstack((image, footer))
    
    def mouse_callback(event, x, y, flags, param):
        nonlocal display_image
        
        # Clear the footer (set to white)
        footer.fill(255)
        
        if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
            # Get BGR values (OpenCV uses BGR format)
            b, g, r = image[y, x]
            
            # Create text for coordinates and BGR values
            coord_text = f'X: {x}, Y: {y}'
            bgr_text = f'B: {b}, G: {g}, R: {r}'
            
            # Put black text in the footer
            cv2.putText(footer, coord_text, (10, 20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)  # Black text
            cv2.putText(footer, bgr_text, (10, 45), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)  # Black text
        
        # Recombine image and footer
        display_image = np.vstack((image, footer))
        cv2.imshow(window_name, display_image)
    
    # Set the mouse callback function
    cv2.setMouseCallback(window_name, mouse_callback)
    
    # Display the initial image
    cv2.imshow(window_name, display_image)
