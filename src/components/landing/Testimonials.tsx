"use client";

import { useRef } from "react";
import { motion, useInView } from "framer-motion";

const testimonials = [
  {
    quote:
      "Organic AI Solutions transformed how we handle customer inquiries. What used to take my team 3 hours a day now runs automatically. We saved over $2,000 a month within the first 60 days.",
    name: "Sarah Mitchell",
    title: "Owner, Mitchell Plumbing & HVAC",
    initials: "SM",
  },
  {
    quote:
      "I was skeptical AI could work for a business our size. They proved me wrong. The process audit alone was eye-opening — I didn't realize how much time we were wasting on things a machine could handle.",
    name: "David Okafor",
    title: "CEO, Okafor Logistics Group",
    initials: "DO",
  },
  {
    quote:
      "The team made AI completely approachable. They trained our non-technical staff, integrated everything into tools we already use, and the ROI was clear within the first month.",
    name: "Jennifer Lau",
    title: "Director of Operations, BrightPath Dental",
    initials: "JL",
  },
];

export default function Testimonials() {
  const ref = useRef(null);
  const inView = useInView(ref, { once: true, margin: "-80px" });

  return (
    <section className="bg-white py-28 px-6 lg:px-10" id="testimonials">
      <div className="max-w-7xl mx-auto" ref={ref}>
        <motion.p
          initial={{ opacity: 0, y: 16 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.45 }}
          className="font-[family-name:var(--font-montserrat)] text-[#E8420A] text-xs font-semibold tracking-widest uppercase mb-4"
        >
          Client Results
        </motion.p>
        <motion.h2
          initial={{ opacity: 0, y: 16 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.45, delay: 0.08 }}
          className="font-[family-name:var(--font-montserrat)] text-4xl md:text-5xl font-bold text-neutral-900 max-w-xl leading-tight mb-16"
          style={{ fontWeight: 700 }}
        >
          Real Businesses. Real Results.
        </motion.h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {testimonials.map((t, i) => (
            <motion.div
              key={t.name}
              initial={{ opacity: 0, y: 28 }}
              animate={inView ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.45, delay: 0.1 + i * 0.08 }}
              className="bg-neutral-50 rounded-2xl p-8 border border-neutral-100 flex flex-col hover:shadow-md hover:-translate-y-0.5 transition-all duration-200"
            >
              {/* Stars */}
              <div className="flex gap-1 mb-5">
                {Array.from({ length: 5 }).map((_, s) => (
                  <svg key={s} width="14" height="14" viewBox="0 0 14 14" fill="#E8420A">
                    <path d="M7 1l1.5 4H13l-3.5 2.5 1.5 4L7 9l-4 2.5 1.5-4L1 5h4.5z" />
                  </svg>
                ))}
              </div>

              <p className="font-[family-name:var(--font-dm-sans)] text-neutral-600 leading-relaxed text-sm flex-1">
                &ldquo;{t.quote}&rdquo;
              </p>

              <div className="mt-7 flex items-center gap-3 pt-6 border-t border-neutral-100">
                <div className="w-9 h-9 rounded-full bg-[#E8420A] flex items-center justify-center shrink-0">
                  <span className="font-[family-name:var(--font-montserrat)] text-white font-bold text-xs">
                    {t.initials}
                  </span>
                </div>
                <div>
                  <div className="font-[family-name:var(--font-montserrat)] font-semibold text-neutral-900 text-sm">
                    {t.name}
                  </div>
                  <div className="font-[family-name:var(--font-dm-sans)] text-neutral-400 text-xs mt-0.5">
                    {t.title}
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
