class FrameworkModel:
    def __init__(self):
        self.languages = {
            "Python": "py", 
            "PHP": "php", 
            "Ruby": "ru", 
            "C": "c",
            "C++": "cpp", 
            "Zig": "zig", 
            "TypeScript": "ts", 
            "JavaScript": "js", 
            "Java": "java", 
            "Node.js": "njs",
            "React": "jtsx",
            "Rust": "rs" 
        }
        self.frameworks = {
            "Python": [
                "FastAPI",
                "Django",
                "Flask",
                "PyTorch",
                "PyQt"
            ],
            "PHP": [
                "Laravel",
                "Symfony",
                "CodeIgniter",
                "CakePHP"
            ],
            "Ruby": [
                "Ruby on Rails",
                "Sinatra",
                "Hanami",
                "Grape"
            ],
            "C/C++": [
                "Qt",
                "wxWidgets",
                "GTK",
                "JUCE",
                "Unreal Engine"
            ],
            "Rust": [
                "Actix Web",
                "Axum",
                "Rocket",
                "Tauri",
                "Bevy"
            ],
            "JavaScript": [
                "React",
                "Vue.js",
                "Angular",
                "Svelte",
                "Astro"
            ],
            "NodeJS": [
                "Express.js",
                "NestJS",
                "Fastify",
                "Koa",
                "Hono"
            ],
            "TypeScript": [
                "Next.js",
                "NestJS",
                "Angular",
                "Nuxt",
                "SvelteKit"
            ],
            "React": [
                "Next.js",
                "React Native",
                "Expo",
                "Gatsby",
                "React Router"
            ],
            "Java": [
                "Spring Boot",
                "Jakarta EE",
                "Quarkus",
                "Micronaut",
                "Hibernate"
            ],
            "Zig": [
                "Jetzig",
                "Zap",
                "httpz",
                "Mach"
            ]
        }
    
    