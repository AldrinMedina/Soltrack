from nicegui import ui 

class HeaderModule:
    def __init__(self):
        # Set page title
        ui.page_title('Soltrack | Smarter Vaccine Logistics')
        
        # Add Google Fonts with extended weights
        ui.add_head_html('<link rel="preconnect" href="https://fonts.googleapis.com">')
        ui.add_head_html('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
        ui.add_head_html('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap">')
        
        # Modern CSS with premium styling
        ui.add_head_html('''
        <style>
            /* Global Styles */
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            
            body { 
                font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                line-height: 1.6;
                color: #1e293b;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                overflow-x: hidden;
            }
            
            /* Enhanced Link Styles */
            .Link {
                color: rgba(255, 255, 255, 0.9);
                text-decoration: none;
                padding: 0.5rem 1rem;
                border-radius: 0.5rem;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                position: relative;
                font-weight: 500;
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                overflow: hidden;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            .Link::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
                transition: left 0.6s ease;
            }
            
            .Link:hover::before {
                left: 100%;
            }
            
            .Link:hover {
                color: #fbbf24;
                background: rgba(255, 255, 255, 0.15);
                transform: translateY(-2px) scale(1.02);
                box-shadow: 0 8px 25px rgba(251, 191, 36, 0.3);
                border-color: rgba(251, 191, 36, 0.4);
                text-shadow: 0 0 20px rgba(251, 191, 36, 0.5);
            }
            
            .Link:active {
                transform: translateY(0) scale(0.98);
            }
            
            /* Premium Animation System */
            .fade-in {
                opacity: 0;
                transform: translateY(30px);
                animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
            }
            
            .fade-in-left {
                opacity: 0;
                transform: translateX(-30px);
                animation: fadeInLeft 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
            }
            
            .fade-in-right {
                opacity: 0;
                transform: translateX(30px);
                animation: fadeInRight 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
            }
            
            .fade-in-scale {
                opacity: 0;
                transform: scale(0.9);
                animation: fadeInScale 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
            }
            
            @keyframes fadeInUp {
                to { 
                    opacity: 1; 
                    transform: translateY(0); 
                }
            }
            
            @keyframes fadeInLeft {
                to { 
                    opacity: 1; 
                    transform: translateX(0); 
                }
            }
            
            @keyframes fadeInRight {
                to { 
                    opacity: 1; 
                    transform: translateX(0); 
                }
            }
            
            @keyframes fadeInScale {
                to { 
                    opacity: 1; 
                    transform: scale(1); 
                }
            }
            
            /* Stagger Animation Delays */
            .fade-in:nth-child(1) { animation-delay: 0.1s; }
            .fade-in:nth-child(2) { animation-delay: 0.2s; }
            .fade-in:nth-child(3) { animation-delay: 0.3s; }
            .fade-in:nth-child(4) { animation-delay: 0.4s; }
            .fade-in:nth-child(5) { animation-delay: 0.5s; }
            
            /* Glass Morphism Components */
            .glass-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
                border-radius: 1rem;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .glass-card:hover {
                background: rgba(255, 255, 255, 0.15);
                transform: translateY(-4px);
                box-shadow: 0 16px 48px rgba(31, 38, 135, 0.5);
            }
            
            /* Premium Button Styles */
            .btn-primary {
                background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
                border: none;
                color: white;
                padding: 0.75rem 2rem;
                border-radius: 0.75rem;
                font-weight: 600;
                font-size: 1rem;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                position: relative;
                overflow: hidden;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
                cursor: pointer;
            }
            
            .btn-primary::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
                transition: left 0.6s ease;
            }
            
            .btn-primary:hover::before {
                left: 100%;
            }
            
            .btn-primary:hover {
                background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
                transform: translateY(-2px) scale(1.02);
                box-shadow: 0 8px 30px rgba(99, 102, 241, 0.4);
            }
            
            .btn-secondary {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 2px solid rgba(255, 255, 255, 0.3);
                color: white;
                padding: 0.75rem 2rem;
                border-radius: 0.75rem;
                font-weight: 600;
                font-size: 1rem;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                cursor: pointer;
            }
            
            .btn-secondary:hover {
                background: rgba(255, 255, 255, 0.2);
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(255, 255, 255, 0.2);
            }
            
            /* Loading and State Indicators */
            .pulse-dot {
                animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
            }
            
            @keyframes pulse {
                0%, 100% { 
                    opacity: 1; 
                    transform: scale(1); 
                }
                50% { 
                    opacity: 0.7; 
                    transform: scale(1.1); 
                }
            }
            
            .loading-shimmer {
                background: linear-gradient(90deg, 
                    rgba(255, 255, 255, 0.1) 0%, 
                    rgba(255, 255, 255, 0.3) 50%, 
                    rgba(255, 255, 255, 0.1) 100%);
                background-size: 200% 100%;
                animation: shimmer 1.5s infinite;
            }
            
            @keyframes shimmer {
                0% { background-position: -200% 0; }
                100% { background-position: 200% 0; }
            }
            
            /* Status Indicators */
            .status-success {
                color: #10b981;
                background: rgba(16, 185, 129, 0.1);
                border: 1px solid rgba(16, 185, 129, 0.3);
                padding: 0.25rem 0.75rem;
                border-radius: 2rem;
                font-size: 0.875rem;
                font-weight: 600;
            }
            
            .status-warning {
                color: #f59e0b;
                background: rgba(245, 158, 11, 0.1);
                border: 1px solid rgba(245, 158, 11, 0.3);
                padding: 0.25rem 0.75rem;
                border-radius: 2rem;
                font-size: 0.875rem;
                font-weight: 600;
            }
            
            .status-error {
                color: #ef4444;
                background: rgba(239, 68, 68, 0.1);
                border: 1px solid rgba(239, 68, 68, 0.3);
                padding: 0.25rem 0.75rem;
                border-radius: 2rem;
                font-size: 0.875rem;
                font-weight: 600;
            }
            
            /* Responsive Design */
            @media (max-width: 768px) {
                body {
                    font-size: 14px;
                }
                
                .Link {
                    padding: 0.4rem 0.8rem;
                    font-size: 0.9rem;
                }
                
                .btn-primary, .btn-secondary {
                    padding: 0.6rem 1.5rem;
                    font-size: 0.9rem;
                }
            }
            
            /* Scroll Enhancement */
            ::-webkit-scrollbar {
                width: 8px;
            }
            
            ::-webkit-scrollbar-track {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 4px;
            }
            
            ::-webkit-scrollbar-thumb {
                background: linear-gradient(135deg, #6366f1, #8b5cf6);
                border-radius: 4px;
                transition: all 0.3s ease;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: linear-gradient(135deg, #7c3aed, #a855f7);
            }
            
            /* Focus Styles for Accessibility */
            .Link:focus-visible,
            .btn-primary:focus-visible,
            .btn-secondary:focus-visible {
                outline: 2px solid #fbbf24;
                outline-offset: 2px;
            }
            
            /* Text Selection */
            ::selection {
                background: rgba(251, 191, 36, 0.3);
                color: white;
            }
        </style>
        ''')

ui.run()