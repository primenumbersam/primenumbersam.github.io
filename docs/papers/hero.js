const bar = document.querySelector('.bar');
const t2 = new SplitText('.txt2').chars;
const t4 = new SplitText('.txt4').chars;

const color1 = '#ffffff';
const color2 = '#17c0fd';

const moveBar = (target) => {
    gsap.set('.bar', {left: gsap.getProperty(target, 'width') + 1});
};

const timeline = gsap.timeline({delay: 0.2});

// === Phase 1: Math ===
timeline
    .set('.txt1', {color: color1, fontWeight: 'regular'})
    .set('.txt2', {color: color2, fontWeight: 'bold', opacity: 0, x: gsap.getProperty('.txt1', 'width') - 2})
    .set('.bar', {left: 1, backgroundColor: color1})

    .to('.bar', {duration: 0.1, opacity: 0, ease: "expo.in", yoyo: true, repeat: 5, repeatDelay: 0.3}, 0)
    .from('.txt1', {duration: 1.1, width: 0, ease: "steps(14)", onUpdate: () => moveBar('.txt1')}, 2.5)
    .to('.bar', {duration: 0.05, backgroundColor: color2}, '+=0.15')
    .to('.bar', {duration: 1.0, width: 390, ease: "power4.inOut"}, '+=0.1')
    .to('.txt2', {duration: 0.01, opacity: 1}, '-=0.1')
    .to('.bar', {duration: 0.4, x: 390, width: 0, ease: "power4.in"})
    .from(t2, {duration: 0.6, opacity: 0, ease: "power3.inOut", stagger: 0.02}, '-=0.5')
    .to('.txt1', {duration: 1.5, opacity: 0.25, ease: "power3.inOut"}, '-=1.2')
    .to('.txt2', {duration: 1.0, opacity: 0}, '+=1.0')

// === Phase 2: Computer ===
    .set('.txt3', {color: color1, fontWeight: 'regular', opacity: 1})
    .set('.txt4', {color: color2, fontWeight: 'bold', opacity: 0, x: gsap.getProperty('.txt3', 'width') - 2})
    .set('.bar', {left: 1, backgroundColor: color1, x: 0, width: 3})

    .to('.txt1', {opacity: 0})
    .from('.txt3', {duration: 1.1, width: 0, ease: "steps(14)", onUpdate: () => moveBar('.txt3')})
    .to('.bar', {duration: 0.05, backgroundColor: color2}, '+=0.1')
    .to('.bar', {duration: 1.0, width: 440, ease: "power4.inOut"}, '+=0.1')
    .to('.txt4', {duration: 0.01, opacity: 1}, '-=0.1')
    .to('.bar', {duration: 0.4, x: 440, width: 0, ease: "power4.in"})
    .from(t4, {duration: 0.6, opacity: 0, ease: "power3.inOut", stagger: 0.02}, '-=0.5')
    .to('.txt3', {duration: 1.5, opacity: 0.25, ease: "power3.inOut"}, '-=1.2')
    .timeScale(1.4);