// Images Open Graph des pages arabes (13/10/2026) — même gabarit que make_og.py (1200×630, fond #0E1420,
// accent #34C47C, tout centré dans la bande carrée de 598 px), mais rendu par CoreText : Pillow, ici sans raqm,
// ne lie pas les lettres arabes. macOS met en forme l'arabe tout seul, sans rien installer.
//
// Usage : swift _build/og_ar.swift _build/og_ar.json [--force]
// og_ar.json : [["ar-hub", "titre", "chiffre ou null", "libellé"], …] → img/og/<slug>.png
import Foundation
import CoreGraphics
import CoreText
import ImageIO
import UniformTypeIdentifiers

let W = 1200, H = 630
let BOX: CGFloat = 630 - 2 * 16            // largeur utile : 598 px (recadrage carré des messageries)
func rgb(_ r: CGFloat, _ g: CGFloat, _ b: CGFloat) -> CGColor { CGColor(red: r / 255, green: g / 255, blue: b / 255, alpha: 1) }
let BG = rgb(14, 20, 32), ACCENT = rgb(52, 196, 124), TITLE = rgb(232, 237, 245), MUTED = rgb(154, 168, 189)

func font(_ bold: Bool, _ size: CGFloat) -> CTFont {
    for name in bold ? ["SFArabic-Bold", "GeezaPro-Bold", "Arial-BoldMT"] : ["SFArabic-Regular", "GeezaPro", "ArialMT"] {
        let f = CTFontCreateWithName(name as CFString, size, nil)
        if (CTFontCopyPostScriptName(f) as String) == name { return f }
    }
    return CTFontCreateWithName((bold ? "Arial-BoldMT" : "ArialMT") as CFString, size, nil)
}

func line(_ text: String, _ f: CTFont, _ color: CGColor) -> CTLine {
    let attrs: [NSAttributedString.Key: Any] = [NSAttributedString.Key(kCTFontAttributeName as String): f,
                                                NSAttributedString.Key(kCTForegroundColorAttributeName as String): color]
    // Une ligne qui contient de l'arabe se lit de droite à gauche, même si elle commence par « TCF Canada » :
    // une marque RLM en tête fixe la direction du paragraphe (sinon « TCF Canada في السعودية » se lit à l'envers).
    let rtl = text.unicodeScalars.contains { (0x0600...0x06FF).contains($0.value) }
    return CTLineCreateWithAttributedString(NSAttributedString(string: rtl ? "\u{200F}" + text : text, attributes: attrs))
}

func width(_ l: CTLine) -> CGFloat { CGFloat(CTLineGetTypographicBounds(l, nil, nil, nil)) }

// Réduit la taille jusqu'à ce que le texte tienne dans la bande (comme fit() de make_og.py).
func fitted(_ text: String, bold: Bool, start: CGFloat, color: CGColor, floor: CGFloat = 22) -> (CTLine, CTFont) {
    var size = start
    while size > floor {
        let f = font(bold, size), l = line(text, f, color)
        if width(l) <= BOX { return (l, f) }
        size -= 2
    }
    let f = font(bold, floor)
    return (line(text, f, color), f)
}

// `top` est le haut de la ligne, comme dans Pillow ; CoreGraphics compte depuis le bas.
func centered(_ ctx: CGContext, _ l: CTLine, _ f: CTFont, top: CGFloat) {
    let x = (CGFloat(W) - width(l)) / 2
    let baseline = CGFloat(H) - top - CTFontGetAscent(f)
    ctx.textPosition = CGPoint(x: x, y: baseline)
    CTLineDraw(l, ctx)
}

func build(_ slug: String, _ title: String, _ stat: String?, _ label: String, outDir: URL) throws {
    let ctx = CGContext(data: nil, width: W, height: H, bitsPerComponent: 8, bytesPerRow: 0,
                        space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.noneSkipLast.rawValue)!
    ctx.setFillColor(BG); ctx.fill(CGRect(x: 0, y: 0, width: W, height: H))
    ctx.setFillColor(ACCENT); ctx.fill(CGRect(x: 0, y: H - 10, width: W, height: 10))          // bandeau supérieur
    let (sur, fs) = fitted("DELF · TCF · TEF", bold: true, start: 30, color: MUTED)
    centered(ctx, sur, fs, top: 74)
    let (t, ft) = fitted(title, bold: true, start: 70, color: TITLE)
    centered(ctx, t, ft, top: 150)
    ctx.setFillColor(ACCENT); ctx.fill(CGRect(x: W / 2 - 46, y: H - 264, width: 92, height: 6))  // filet sous le titre
    if let stat = stat {
        let (s, fst) = fitted(stat, bold: true, start: 112, color: ACCENT)
        centered(ctx, s, fst, top: 310)
        let (lb, fl) = fitted(label, bold: false, start: 34, color: MUTED)
        centered(ctx, lb, fl, top: 452)
    } else {
        let (lb, fl) = fitted(label, bold: false, start: 36, color: MUTED)
        centered(ctx, lb, fl, top: 330)
    }
    let dom = line("delf-tcf-tef.fr", font(false, 28), ACCENT)
    centered(ctx, dom, font(false, 28), top: 556)
    let url = outDir.appendingPathComponent(slug + ".png")
    guard let img = ctx.makeImage(),
          let dest = CGImageDestinationCreateWithURL(url as CFURL, UTType.png.identifier as CFString, 1, nil) else {
        throw NSError(domain: "og_ar", code: 1)
    }
    CGImageDestinationAddImage(dest, img, nil)
    guard CGImageDestinationFinalize(dest) else { throw NSError(domain: "og_ar", code: 2) }
}

let args = CommandLine.arguments
guard args.count >= 2 else { print("usage : swift og_ar.swift og_ar.json [--force]"); exit(2) }
let force = args.contains("--force")
let here = URL(fileURLWithPath: args[1]).deletingLastPathComponent()
let outDir = here.appendingPathComponent("../img/og").standardizedFileURL
let entries = try JSONSerialization.jsonObject(with: Data(contentsOf: URL(fileURLWithPath: args[1]))) as! [[Any]]
var made: [String] = [], kept: [String] = []
for e in entries {
    let slug = e[0] as! String, title = e[1] as! String, stat = e[2] as? String, label = e[3] as! String
    if FileManager.default.fileExists(atPath: outDir.appendingPathComponent(slug + ".png").path) && !force {
        kept.append(slug); continue
    }
    try build(slug, title, stat, label, outDir: outDir)
    made.append(slug)
}
print("générées : " + (made.isEmpty ? "(aucune)" : made.joined(separator: ", ")))
if !kept.isEmpty { print("déjà présentes : " + kept.joined(separator: ", ")) }
